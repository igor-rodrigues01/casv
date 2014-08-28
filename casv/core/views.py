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
    imported_polygons = 0

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
                            code=feature['properties']['id'],
                            area_ha=feature['properties']['area_ha'],
                            n_proc=feature['properties']['n_proc'],
                            reservator=feature['properties']['reservator'],
                            typology=feature['properties']['tipologia'],
                            user=user
                            )
                        asv.save()
                        imported_polygons += 1

                rmtree(upload_path)
                msg = _('Imported %s polygons') % imported_polygons

                return redirect(reverse('core:upload_success'))
            else:
                msg = _('We did not find a shape file in the zip file.')
    else:
        msg = _('Uploaded file is not a valid zip file.')


def upload_file(request):
    '''View that renders and processes the upload files form.'''

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['upload_file'], request.user)

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