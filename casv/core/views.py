import zipfile
import fiona

from datetime import datetime
from collections import OrderedDict
from os import path, mkdir
from shutil import rmtree

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Polygon
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from django.contrib.auth.models import User

from .forms import UploadFileForm
from .models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica


class InvalidShapefileError(Exception):
    pass


def get_mapping(schema):
    asv = {'properties': OrderedDict([('codigo', 'int:10'), ('n_autex', 'str:30'),
        ('uf', 'str:2'), ('fito', 'str:60'), ('nom_prop', 'str:60'),
        ('cpfj_prop', 'str:22'), ('detentor', 'str:60'), ('cpfj_dete', 'str:22'),
        ('rt', 'str:60'), ('cpfj_rt', 'str:22'), ('area_ha', 'float:24.15'),
        ('lenha_st', 'float:24.15'), ('tora_m', 'float:24.15'),
        ('torete_m', 'float:24.15'), ('mourao_m', 'float:24.15'),
        ('data_autex', 'date'), ('valido_ate', 'date'),
        ('municipio', 'str:40')]), 'geometry': 'Polygon'}
    mapping_asv = {
            'codigo': 'codigo',
            'n_autex': 'n_autex',
            'uf': 'uf',
            'fito': 'fito',
            'nom_prop': 'nom_prop',
            'cpfj_prop': 'cpfj_prop',
            'detentor': 'detentor',
            'cpfj_dete': 'cpfj_dete',
            'rt': 'rt',
            'cpfj_rt': 'cpfj_rt',
            'area_ha': 'area_ha',
            'lenha_st': 'lenha_st',
            'tora_m': 'tora_m',
            'torete_m': 'torete_m',
            'mourao_m': 'mourao_m',
            'data_autex': 'data_autex',
            'valido_ate': 'valido_ate',
            'municipio': 'municipio',
    }

    asv_mata_atlantica = {'properties': OrderedDict([('processo', 'int:10'),
        ('empreended', 'str:254'), ('uf', 'str:2'), ('municipio', 'str:254'),
        ('tipo_empre', 'str:254'), ('cpfj', 'str:22'), ('area_total', 'float:24.15'),
        ('a_veg_prim', 'float:24.15'), ('a_est_medi', 'float:24.15'),
        ('a_est_avan', 'float:24.15')]), 'geometry': 'Polygon'}
    mapping_asv_mata_atlantica = {
            'processo': 'processo',
            'uf': 'uf',
            'municipio': 'municipio',
            'empreendedor': 'empreended',
            'tipo_empreendimento': 'tipo_empre',
            'cpfj': 'cpfj',
            'area_supressao_total': 'area_total',
            'area_supressao_veg_primaria': 'a_veg_prim',
            'area_supressao_estagio_medio': 'a_est_medi',
            'area_supressao_estagio_avancado': 'a_est_avan',
    }

    compensacao = {'properties': OrderedDict([('processo', 'int:10'),
        ('empreended', 'str:254'), ('uf', 'str:2'), ('municipio', 'str:254'),
        ('tipo_empre', 'str:254'), ('cpfj', 'str:22'),
        ('area_compe', 'float:24.15')]), 'geometry': 'Polygon'}
    mapping_compensacao = {
            'processo': 'processo',
            'uf': 'uf',
            'municipio': 'municipio',
            'empreendedor': 'empreended',
            'tipo_empreendimento': 'tipo_empre',
            'cpfj': 'cpfj',
            'area_compensacao': 'area_compe',
    }

    area_soltura = {'geometry': 'Polygon',
        'properties': OrderedDict([('processo', 'int:10'), ('nome', 'str:254'),
        ('endereco', 'str:254'), ('uf', 'str:2'), ('municipio', 'str:254'),
        ('proprietar', 'str:254'), ('cpf', 'str:11'), ('telefone', 'str:15'),
        ('email', 'str:254'), ('area', 'float:24.15'), ('arl_app', 'float:24.15'),
        ('bioma', 'str:254'), ('fitofision', 'str:254'), ('conservaca', 'int:1'),
        ('conectivid', 'int:1'), ('uc', 'int:1'), ('agua', 'int:1'),
        ('atividade', 'str:254'), ('documento', 'int:1'), ('mapa', 'int:1'),
        ('carta', 'int:1'), ('reabilitad', 'int:1'), ('viveiros', 'int:5'),
        ('distancia', 'float:24.15'), ('tempo', 'float:24.15'),
        ('vistoria', 'date')])
    }
    mapping_area_soltura = {
            'processo': 'processo',
            'nome': 'nome',
            'endereco': 'endereco',
            'uf': 'uf',
            'municipio': 'municipio',
            'proprietario': 'proprietar',
            'cpf': 'cpf',
            'telefone': 'telefone',
            'email': 'email',
            'area': 'area',
            'arl_app': 'arl_app',
            'bioma': 'bioma',
            'fitofisionomia': 'fitofision',
            'conservacao': 'conservaca',
            'conectividade': 'conectivid',
            'uc': 'uc',
            'agua': 'agua',
            'atividade': 'atividade',
            'documento': 'documento',
            'mapa': 'mapa',
            'carta': 'carta',
            'reabilitador': 'reabilitad',
            'viveiros': 'viveiros',
            'distancia': 'distancia',
            'tempo': 'tempo',
            'vistoria': 'vistoria',
    }

    if schema == asv:
        return [Asv, mapping_asv, 'Asv']
    elif schema == area_soltura:
        return [AreaSoltura, mapping_area_soltura, 'AreaSoltura']
    elif schema == asv_mata_atlantica:
        return [AsvMataAtlantica, mapping_asv_mata_atlantica, 'AsvMataAtlantica']
    elif schema == compensacao:
        return [CompensacaoMataAtlantica, mapping_compensacao,
            'CompensacaoMataAtlantica']
    else:
        raise InvalidShapefileError(
            _('The shapefile is not in one of the accepted schemas.')
        )


def handle_uploaded_file(file, user):
    '''Function to process a uploaded file, test if it is a valid zip file and
    if it has a .shp file within, convert the shp file to geojson and import it,
    creating a new Asv file'''

    upload_folder = 'media/'
    upload_path = path.join(upload_folder,
        user.username + datetime.now().strftime('%f')
        )

    if zipfile.is_zipfile(file):
        shp_zip = zipfile.ZipFile(file)
        shp = [filename for filename in shp_zip.namelist() if filename[-3:].lower() == 'shp']
        if len(shp) == 1:
            mkdir(upload_path)
            shp_zip.extractall(upload_path)
            shp_file = fiona.open(path=path.join(upload_path, shp[0]))

            model, mapping, type_str = get_mapping(shp_file.schema)
            number_of_features = len(shp_file)

            for i in range(number_of_features):
                feature = shp_file.next()
                dict_data = dict(zip(
                    mapping.keys(),
                    [feature['properties'].get(v) for v in mapping.values()]
                ))

                entry = model(**dict_data)
                entry.geom = Polygon(feature['geometry']['coordinates'][0])
                entry.usuario = user
                entry.save()

            rmtree(upload_path)

            return {'type': type_str, 'quantity': number_of_features}


def upload_file(request):
    '''View that renders and processes the upload files form.'''

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                upload_return = handle_uploaded_file(
                    request.FILES['upload_file'],
                    request.user
                )

                context = {
                    'uploaded': True,
                    'success': True,
                    'quantity': upload_return.get('quantity'),
                    'type': upload_return.get('type'),
                    'form': form
                }
            except InvalidShapefileError:
                context = {'uploaded': True, 'success': False, 'form': form}

    else:
        context = {'form': UploadFileForm()}

    return render(request, 'core/upload.html', context)


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

    return render(request, 'core/login_page.html', {'msg': msg})


def logout_view(request):
    logout(request)
    return redirect(reverse('core:index'))


class UserUploads(DetailView):

    model = User
    template_name = 'core/user_uploads.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserUploads, self).get_context_data(**kwargs)
        return context


class AsvDetailView(DetailView):
    model = Asv
    context_object_name = 'asv'


class AreaSolturaDetailView(DetailView):
    model = AreaSoltura
    context_object_name = 'areasoltura'


class AsvMaDetailView(DetailView):
    model = AsvMataAtlantica
    context_object_name = 'asvma'


class CompensacaoDetailView(DetailView):
    model = CompensacaoMataAtlantica
    context_object_name = 'compensacao'


