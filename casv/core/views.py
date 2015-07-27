import zipfile
from datetime import datetime
import fiona

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

    if zipfile.is_zipfile(file):
        zip = zipfile.ZipFile(file)
        shp = [filename for filename in zip.namelist() if filename[-3:].lower() == 'shp']
        if len(shp) == 1:
            shp_file = fiona.open(path='/%s' % shp[0], vfs='zip://%s' % file)

            for i in range(len(shp_file)):
                feature = shp_file.next()
                if feature['geometry'].get('type') == 'Polygon':
                    asv = Asv(
                        geom=Polygon(feature['geometry']['coordinates'][0]),
                        usuario=user,
                    )
                    if feature['properties'].get('Id'):
                        asv.codigo = feature['properties'].get('Id')
                    if feature['properties'].get('n_autex'):
                        asv.n_autex = feature['properties'].get('n_autex')
                    if feature['properties'].get('uf'):
                        asv.uf = feature['properties'].get('uf')
                    if feature['properties'].get('fito'):
                        asv.fito = feature['properties'].get('fito')
                    if feature['properties'].get('nom_prop'):
                        asv.nom_prop = feature['properties'].get('nom_prop')
                    if feature['properties'].get('cpfj_prop'):
                        asv.cpfj_prop = feature['properties'].get('cpfj_prop')
                    if feature['properties'].get('detentor'):
                        asv.detentor = feature['properties'].get('detentor')
                    if feature['properties'].get('cpfj_dete'):
                        asv.cpfj_dete = feature['properties'].get('cpfj_dete')
                    if feature['properties'].get('rt'):
                        asv.rt = feature['properties'].get('rt')
                    if feature['properties'].get('cpfj_rt'):
                        asv.cpfj_rt = feature['properties'].get('cpfj_rt')
                    if feature['properties'].get('area_ha'):
                        asv.area_ha = feature['properties'].get('area_ha')
                    if feature['properties'].get('lenha_st'):
                        asv.lenha_st = feature['properties'].get('lenha_st')
                    if feature['properties'].get('tora_m'):
                        asv.tora_m = feature['properties'].get('tora_m')
                    if feature['properties'].get('torete_m'):
                        asv.torete_m = feature['properties'].get('torete_m')
                    if feature['properties'].get('mourao_m'):
                        asv.mourao_m = feature['properties'].get('mourao_m')
                    if feature['properties'].get('municipio'):
                        asv.municipio = feature['properties'].get('municipio')
                    if feature['properties'].get('data_autex'):
                        asv.data_autex = datetime.strptime(
                            feature['properties'].get('data_autex'), '%Y-%m-%d'
                        )
                    if feature['properties'].get('valido_ate'):
                        asv.valido_ate = datetime.strptime(
                            feature['properties'].get('valido_ate'), '%Y-%m-%d'
                        )
                    asv.save()


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