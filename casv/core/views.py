import simplejson

import zipfile
from subprocess import call
from os import path, mkdir
from datetime import datetime
from shutil import rmtree

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Polygon
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from django.contrib.auth.models import User

from .forms import UploadFileForm
from .models import Asv


def handle_uploaded_file(file, user):
    '''Function to process a uploaded file, test if it is a valid zip file and
    if it has a .shp file within, convert the shp file to geojson and import it,
    creating a new Asv file'''

    upload_folder = 'media/'
    upload_path = path.join(upload_folder,
        user.username + datetime.now().strftime('%f')
        )

    if zipfile.is_zipfile(file):
        zip = zipfile.ZipFile(file)
        for filename in zip.namelist():
            if filename[-3:].lower() == 'shp':
                mkdir(upload_path)
                zip.extractall(upload_path)
                call(['ogr2ogr',
                    '-f', 'GeoJSON',
                    '-t_srs', 'EPSG:4674',
                    path.join(upload_path, filename[:-3] + 'geojson'),
                    path.join(upload_path, filename)
                    ])

                data_json = open(
                    path.join(upload_path, filename[:-3] + 'geojson'), 'r'
                    ).read()
                data = simplejson.loads(data_json)
                for feature in data['features']:
                    if feature['geometry'].get('type') == 'Polygon':
                        asv = Asv(
                            polygon=Polygon(feature['geometry']['coordinates'][0]),
                            user=user
                            )
                        if feature['properties'].get('Id') is not None:
                            asv.code = feature['properties'].get('Id')
                        if feature['properties'].get('n_autex') is not None:
                            asv.n_autex = feature['properties'].get('n_autex')
                        if feature['properties'].get('uf') is not None:
                            asv.uf = feature['properties'].get('uf')
                        if feature['properties'].get('fito') is not None:
                            asv.fito = feature['properties'].get('fito')
                        if feature['properties'].get('nom_prop') is not None:
                            asv.nom_prop = feature['properties'].get('nom_prop')
                        if feature['properties'].get('cpfj_prop') is not None:
                            asv.cpfj_prop = feature['properties'].get('cpfj_prop')
                        if feature['properties'].get('detentor') is not None:
                            asv.detentor = feature['properties'].get('detentor')
                        if feature['properties'].get('cpfj_dete') is not None:
                            asv.cpfj_dete = feature['properties'].get('cpfj_dete')
                        if feature['properties'].get('rt') is not None:
                            asv.rt = feature['properties'].get('rt')
                        if feature['properties'].get('cpfj_rt') is not None:
                            asv.cpfj_rt = feature['properties'].get('cpfj_rt')
                        if feature['properties'].get('area_ha') is not None:
                            asv.area_ha = feature['properties'].get('area_ha')
                        if feature['properties'].get('lenha_st') is not None:
                            asv.lenha_st = feature['properties'].get('lenha_st')
                        if feature['properties'].get('tora_m') is not None:
                            asv.tora_m = feature['properties'].get('tora_m')
                        if feature['properties'].get('torete_m') is not None:
                            asv.torete_m = feature['properties'].get('torete_m')
                        if feature['properties'].get('mourao_m') is not None:
                            asv.mourao_m = feature['properties'].get('mourao_m')
                        if feature['properties'].get('municipio') is not None:
                            asv.municipio = feature['properties'].get('municipio')
                        if feature['properties'].get('data_autex') is str():
                            asv.data_autex = feature['properties'].get('data_autex').replace('/', '-')
                        if feature['properties'].get('valido_ate') is str():
                            asv.valido_ate = feature['properties'].get('valido_ate').replace('/', '-'),
                        asv.save()

                rmtree(upload_path)


def upload_file(request):
    '''View that renders and processes the upload files form.'''

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['upload_file'], request.user)
            return redirect(reverse('core:upload_success'))
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})


def login_view(request):
    msg = _('Please log in below...')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('core:index'))
            else:
                msg = _('Your account is not active. Please contact the system administrator')
                return redirect(reverse('core:login'))
        else:
            msg = _('Invalid username or password.')
            return render(request, 'login_page.html', {'msg': msg})

    return render(request, 'login_page.html', {'msg': msg})


def logout_view(request):
    logout(request)
    return redirect(reverse('core:index'))


class UserUploads(DetailView):

    model = User
    template_name = 'user_uploads.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserUploads, self).get_context_data(**kwargs)
        return context