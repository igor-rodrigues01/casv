import zipfile
import fiona

from datetime import datetime
from collections import OrderedDict
from os import path, mkdir
from shutil import rmtree

from rest_framework.generics import RetrieveAPIView
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.gis.geos import Polygon, MultiPolygon
from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView
from django.utils.translation import ugettext as _
from shapely.geometry.base import BaseGeometry
from shapely.geometry import shape
from .forms import UploadFileForm
from .models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica
from .models import AutoInfracaoOEMA, EmbargoOEMA
from .serializers import CompensacaoSerializer, AsvMaSerializer
from .serializers import AsvSerializer, SolturaSerializer
from .serializers import EmbargoSerializer, AutoInfracaoSerializer


class InvalidShapefileError(Exception):

    def __init__(self, message):
        self.message = message


def get_mapping(schema):
    asv = {
        'properties': OrderedDict([
            ('codigo', 'int:10'),
            ('n_autex', 'str:30'),
            ('uf', 'str:2'),
            ('fito', 'str:60'),
            ('nom_prop', 'str:60'),
            ('cpfj_prop', 'str:22'),
            ('detentor', 'str:60'),
            ('cpfj_dete', 'str:22'),
            ('rt', 'str:60'),
            ('cpfj_rt', 'str:22'),
            ('area_ha', 'float:20.15'),
            ('lenha_st', 'float:20.15'),
            ('tora_m', 'float:20.15'),
            ('torete_m', 'float:20.15'),
            ('mourao_m', 'float:20.15'),
            ('data_autex', 'date'),
            ('valido_ate', 'date'),
            ('municipio', 'str:40')
        ]),
        'geometry': 'Polygon'
    }

    asv2 = {
        'properties': OrderedDict([
            ('codigo', 'int:10'),
            ('n_autex', 'str:30'),
            ('uf', 'str:2'),
            ('fito', 'str:60'),
            ('nom_prop', 'str:60'),
            ('cpfj_prop', 'str:22'),
            ('detentor', 'str:60'),
            ('cpfj_dete', 'str:22'),
            ('rt', 'str:60'),
            ('cpfj_rt', 'str:22'),
            ('area_ha', 'float:20.15'),
            ('lenha_st', 'float:20.15'),
            ('tora_m', 'float:20.15'),
            ('torete_m', 'float:20.15'),
            ('mourao_m', 'float:20.15'),
            ('data_autex', 'date'),
            ('valido_ate', 'date'),
            ('municipio', 'str:40')
        ]),
        'geometry': 'Multipolygon'
    }

    asv3 = {
        'properties': OrderedDict([
            ('codigo', 'int:9'),
            ('n_autex', 'str:30'),
            ('uf', 'str:2'),
            ('fito', 'str:60'),
            ('nom_prop', 'str:60'),
            ('cpfj_prop', 'str:22'),
            ('detentor', 'str:60'),
            ('cpfj_dete', 'str:22'),
            ('rt', 'str:60'),
            ('cpfj_rt', 'str:22'),
            ('area_ha', 'float:20'),
            ('lenha_st', 'float:20'),
            ('tora_m', 'float:20'),
            ('torete_m', 'float:20'),
            ('mourao_m', 'float:20'),
            ('data_autex', 'date'),
            ('valido_ate', 'date'),
            ('municipio', 'str:40')
        ]),
        'geometry': 'Polygon'
    }

    asv4 = {
        'properties': OrderedDict([
            ('codigo', 'int:9'),
            ('n_autex', 'str:30'),
            ('uf', 'str:2'),
            ('fito', 'str:60'),
            ('nom_prop', 'str:60'),
            ('cpfj_prop', 'str:22'),
            ('detentor', 'str:60'),
            ('cpfj_dete', 'str:22'),
            ('rt', 'str:60'),
            ('cpfj_rt', 'str:22'),
            ('area_ha', 'float:20'),
            ('lenha_st', 'float:20'),
            ('tora_m', 'float:20'),
            ('torete_m', 'float:20'),
            ('mourao_m', 'float:20'),
            ('data_autex', 'date'),
            ('valido_ate', 'date'),
            ('municipio', 'str:40')
        ]),
        'geometry': 'Multipolygon'
    }


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

    asv_mata_atlantica = {
        'properties': OrderedDict([
            ('processo', 'int:10'),
            ('empreended', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('tipo_empre', 'str:254'),
            ('cpfj', 'str:22'),
            ('area_total', 'float:20.15'),
            ('a_veg_prim', 'float:20.15'),
            ('a_est_medi', 'float:20.15'),
            ('a_est_avan', 'float:20.15')
        ]),
        'geometry': 'Polygon'
    }

    asv_mata_atlantica2 = {
        'properties': OrderedDict([
            ('processo', 'int:10'),
            ('empreended', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('tipo_empre', 'str:254'),
            ('cpfj', 'str:22'),
            ('area_total', 'float:20.15'),
            ('a_veg_prim', 'float:20.15'),
            ('a_est_medi', 'float:20.15'),
            ('a_est_avan', 'float:20.15')
        ]),
        'geometry': 'Multipolygon'
    }

    asv_mata_atlantica3 = {
        'properties': OrderedDict([
            ('processo', 'int:9'),
            ('empreended', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('tipo_empre', 'str:254'),
            ('cpfj', 'str:22'),
            ('area_total', 'float:20'),
            ('a_veg_prim', 'float:20'),
            ('a_est_medi', 'float:20'),
            ('a_est_avan', 'float:20')
        ]),
        'geometry': 'Polygon'
    }

    asv_mata_atlantica4 = {
        'properties': OrderedDict([
            ('processo', 'int:9'),
            ('empreended', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('tipo_empre', 'str:254'),
            ('cpfj', 'str:22'),
            ('area_total', 'float:20'),
            ('a_veg_prim', 'float:20'),
            ('a_est_medi', 'float:20'),
            ('a_est_avan', 'float:20')
        ]),
        'geometry': 'Multipolygon'
    }

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

    compensacao = {
        'properties': OrderedDict([
            ('processo', 'int:10'),
            ('empreended', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('tipo_empre', 'str:254'),
            ('cpfj', 'str:22'),
            ('area_compe', 'float:20.15')
        ]),
        'geometry': 'Polygon'
    }

    compensacao2 = {
        'properties': OrderedDict([
            ('processo', 'int:10'),
            ('empreended', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('tipo_empre', 'str:254'),
            ('cpfj', 'str:22'),
            ('area_compe', 'float:20.15')
        ]),
        'geometry': 'Multipolygon'
    }

    compensacao3 = {
        'properties': OrderedDict([
            ('processo', 'int:9'),
            ('empreended', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('tipo_empre', 'str:254'),
            ('cpfj', 'str:22'),
            ('area_compe', 'float:20')
        ]),
        'geometry': 'Polygon'
    }

    compensacao4 = {
        'properties': OrderedDict([
            ('processo', 'int:9'),
            ('empreended', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('tipo_empre', 'str:254'),
            ('cpfj', 'str:22'),
            ('area_compe', 'float:20')
        ]),
        'geometry': 'Multipolygon'
    }

    mapping_compensacao = {
        'processo': 'processo',
        'uf': 'uf',
        'municipio': 'municipio',
        'empreendedor': 'empreended',
        'tipo_empreendimento': 'tipo_empre',
        'cpfj': 'cpfj',
        'area_compensacao': 'area_compe',
    }

    area_soltura = {
        'geometry': 'Polygon',
        'properties': OrderedDict([
            ('processo', 'int:10'),
            ('nome', 'str:254'),
            ('endereco', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('proprietar', 'str:254'),
            ('cpf', 'str:11'),
            ('telefone', 'str:15'),
            ('email', 'str:254'),
            ('area', 'float:20.15'),
            ('arl_app', 'float:20.15'),
            ('bioma', 'str:254'),
            ('fitofision', 'str:254'),
            ('conservaca', 'int:1'),
            ('conectivid', 'int:1'),
            ('uc', 'int:1'),
            ('agua', 'int:1'),
            ('atividade', 'str:254'),
            ('documento', 'int:1'),
            ('mapa', 'int:1'),
            ('carta', 'int:1'),
            ('reabilitad', 'int:1'),
            ('viveiros', 'int:5'),
            ('distancia', 'float:20.15'),
            ('tempo', 'str:5'),
            ('vistoria', 'date'),
            ('taxon', 'str:254')])
    }

    area_soltura2 = {
        'geometry': 'Multipolygon',
        'properties': OrderedDict([
            ('processo', 'int:10'),
            ('nome', 'str:254'),
            ('endereco', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('proprietar', 'str:254'),
            ('cpf', 'str:11'),
            ('telefone', 'str:15'),
            ('email', 'str:254'),
            ('area', 'float:20.15'),
            ('arl_app', 'float:20.15'),
            ('bioma', 'str:254'),
            ('fitofision', 'str:254'),
            ('conservaca', 'int:1'),
            ('conectivid', 'int:1'),
            ('uc', 'int:1'),
            ('agua', 'int:1'),
            ('atividade', 'str:254'),
            ('documento', 'int:1'),
            ('mapa', 'int:1'),
            ('carta', 'int:1'),
            ('reabilitad', 'int:1'),
            ('viveiros', 'int:5'),
            ('distancia', 'float:20.15'),
            ('tempo', 'str:5'),
            ('vistoria', 'date'),
            ('taxon', 'str:254')])
    }

    area_soltura3 = {
        'geometry': 'Multipolygon',
        'properties': OrderedDict([
            ('processo', 'int:9'),
            ('nome', 'str:254'),
            ('endereco', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('proprietar', 'str:254'),
            ('cpf', 'str:11'),
            ('telefone', 'str:15'),
            ('email', 'str:254'),
            ('area', 'float:20.15'),
            ('arl_app', 'float:20.15'),
            ('bioma', 'str:254'),
            ('fitofision', 'str:254'),
            ('conservaca', 'int:1'),
            ('conectivid', 'int:1'),
            ('uc', 'int:1'),
            ('agua', 'int:1'),
            ('atividade', 'str:254'),
            ('documento', 'int:1'),
            ('mapa', 'int:1'),
            ('carta', 'int:1'),
            ('reabilitad', 'int:1'),
            ('viveiros', 'int:5'),
            ('distancia', 'float:20.15'),
            ('tempo', 'str:5'),
            ('vistoria', 'date'),
            ('taxon', 'str:254')])
    }
    area_soltura4 = {
        'geometry': 'Polygon',
        'properties': OrderedDict([
            ('processo', 'int:9'),
            ('nome', 'str:254'),
            ('endereco', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('proprietar', 'str:254'),
            ('cpf', 'str:11'),
            ('telefone', 'str:15'),
            ('email', 'str:254'),
            ('area', 'float:20.15'),
            ('arl_app', 'float:20.15'),
            ('bioma', 'str:254'),
            ('fitofision', 'str:254'),
            ('conservaca', 'int:1'),
            ('conectivid', 'int:1'),
            ('uc', 'int:1'),
            ('agua', 'int:1'),
            ('atividade', 'str:254'),
            ('documento', 'int:1'),
            ('mapa', 'int:1'),
            ('carta', 'int:1'),
            ('reabilitad', 'int:1'),
            ('viveiros', 'int:5'),
            ('distancia', 'float:20.15'),
            ('tempo', 'str:5'),
            ('vistoria', 'date'),
            ('taxon', 'str:254')])
    }

    area_soltura5 = {
        'geometry': 'Polygon',
        'properties': OrderedDict([
            ('processo', 'int:9'),
            ('nome', 'str:254'),
            ('endereco', 'str:254'),
            ('uf', 'str:2'),
            ('municipio', 'str:254'),
            ('proprietar', 'str:254'),
            ('cpf', 'str:11'),
            ('telefone', 'str:15'),
            ('email', 'str:254'),
            ('area', 'float:20'),
            ('arl_app', 'float:20'),
            ('bioma', 'str:254'),
            ('fitofision', 'str:254'),
            ('conservaca', 'int:9'),
            ('conectivid', 'int:9'),
            ('uc', 'int:9'),
            ('agua', 'int:9'),
            ('atividade', 'str:254'),
            ('documento', 'int:9'),
            ('mapa', 'int:9'),
            ('carta', 'int:9'),
            ('reabilitad', 'int:9'),
            ('viveiros', 'int:9'),
            ('distancia', 'float:20'),
            ('tempo', 'str:5'),
            ('vistoria', 'date'),
            ('taxon', 'str:254')])
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
        'taxon': 'taxon',
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

    auto_infracao = {
        'properties': OrderedDict([
            ('proc', 'str:30'),
            ('num_ai', 'str:20'),
            ('num_tei', 'str:20'),
            ('area_ha', 'float:9.2'),
            ('desc', 'str:254'),
            ('legislacao', 'str:100'),
            ('status', 'str:100'),
            ('nome', 'str:100'),
            ('cpfj', 'str:20'),
            ('municipio', 'str:250')
        ]),
        'geometry': 'Polygon'
    }

    auto_infracao2 = {
        'properties': OrderedDict([
            ('proc', 'str:30'),
            ('num_ai', 'str:20'),
            ('num_tei', 'str:20'),
            ('area_ha', 'float:9.2'),
            ('desc', 'str:254'),
            ('legislacao', 'str:100'),
            ('status', 'str:100'),
            ('nome', 'str:100'),
            ('cpfj', 'str:20'),
            ('municipio', 'str:250')
        ]),
        'geometry': 'Multipolygon'
    }

    mapping_auto_infracao = {
        'proc': 'proc',
        'num_ai': 'num_ai',
        'num_tei': 'num_tei',
        'area_ha': 'area_ha',
        'desc': 'desc',
        'legislacao': 'legislacao',
        'nome': 'nome',
        'cpfj': 'cpfj',
        'municipio': 'municipio',
        'status': 'status'
    }

    embargo_oema = {
        'properties': OrderedDict([
            ('proc', 'str:30'),
            ('num_ai', 'str:20'),
            ('num_tei', 'str:20'),
            ('area_ha', 'float:9.2'),
            ('desc', 'str:254'),
            ('legislacao', 'str:100'),
            ('nome', 'str:100'),
            ('cpfj', 'str:20'),
            ('municipio', 'str:250'),
            ('status', 'str:100')
        ]),
        'geometry': 'Polygon'
    }

    embargo_oema2 = {
        'properties': OrderedDict([
            ('proc', 'str:30'),
            ('num_ai', 'str:20'),
            ('num_tei', 'str:20'),
            ('area_ha', 'float:9.2'),
            ('desc', 'str:254'),
            ('legislacao', 'str:100'),
            ('nome', 'str:100'),
            ('cpfj', 'str:20'),
            ('municipio', 'str:250'),
            ('status', 'str:100')
        ]),
        'geometry': 'Multipolygon'
    }

    mapping_embargo_oema = {
        'proc': 'proc',
        'num_ai': 'num_ai',
        'num_tei': 'num_tei',
        'area_ha': 'area_ha',
        'desc': 'desc',
        'legislacao': 'legislacao',
        'nome': 'nome',
        'cpfj': 'cpfj',
        'municipio': 'municipio',
        'status': 'status'
    }
   
    if schema == asv or schema == asv2 or schema == asv3:
        return [Asv, mapping_asv, 'Asv']
    elif schema == area_soltura or schema == area_soltura2 or \
        schema == area_soltura3 or schema == area_soltura4 or schema == area_soltura5:
        return [AreaSoltura, mapping_area_soltura, 'AreaSoltura']
    elif schema == asv_mata_atlantica or schema == asv_mata_atlantica2 \
        or schema == asv_mata_atlantica3 or schema == asv_mata_atlantica4 :
        return [AsvMataAtlantica, mapping_asv_mata_atlantica,
                'AsvMataAtlantica']
    elif schema == compensacao or schema == compensacao2 or schema == compensacao3 \
        or schema == compensacao3:
        return [CompensacaoMataAtlantica, mapping_compensacao,
                'CompensacaoMataAtlantica']
    elif schema == embargo_oema or schema == embargo_oema2:
        return [EmbargoOEMA, mapping_embargo_oema, 'EmbargoOEMA']
    elif schema == auto_infracao or schema == auto_infracao2:
        return [AutoInfracaoOEMA, mapping_auto_infracao, 'AutoInfracaoOEMA']
    else:
        raise InvalidShapefileError(
            _('The shapefile is not in one of the accepted schemas.')
        )


def handle_uploaded_file(file, user):
    '''Function to process a uploaded file, test if it is a valid zip file and
    if it has a .shp file within, convert the shp file to geojson and import
    it, creating a new Asv file'''

    upload_folder = 'media/'
    upload_path = path.join(
        upload_folder,
        user.username + datetime.now().strftime('%f'))
    if zipfile.is_zipfile(file):
        shp_zip = zipfile.ZipFile(file)
        shp = [filename for filename in shp_zip.namelist() if filename[-3:].lower() == 'shp']
        if len(shp) == 1:
            mkdir(upload_path)
            shp_zip.extractall(upload_path)
            shp_file = fiona.open(path=path.join(upload_path, shp[0]))
            try:  
                model, mapping, type_str = get_mapping(shp_file.schema)
            except IndexError as error:
                raise InvalidShapefileError(
                    _('O arquivo shape não é valido, pode ocorrer devido  algum erro nos campos que compõe o schema do arquivo.')
                )
            number_of_features = len(shp_file)
            for i in range(number_of_features):
                feature = shp_file.next()
                dict_data = dict(zip(
                    mapping.keys(),
                    [feature['properties'].get(v) for v in mapping.values()]))
                entry = model(**dict_data)
                if feature['geometry']['type'] == 'Polygon':
                    entry.geom = MultiPolygon(Polygon(feature['geometry']['coordinates'][0]))
                else:
                    multipolygon = shape(feature['geometry'])
                    try:
                        entry.geom = multipolygon.wkt
                    except TypeError:
                         raise InvalidShapefileError(_('O arquivo contém geometria inválida.'))               
                entry.usuario = user
                entry.save()

            rmtree(upload_path)
            return {'type': type_str, 'quantity': number_of_features}
        else:
            raise InvalidShapefileError(
                _('There is not a .shp file inside of the zip file.'))
    else:
        raise InvalidShapefileError(_('The uploaded file is not a zip file.'))


def upload_file(request):
    '''View that renders and processes the upload files form.'''

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                upload_return = handle_uploaded_file(
                    request.FILES['upload_file'],
                    request.user)

                context = {
                    'uploaded': True,
                    'success': True,
                    'quantity': upload_return.get('quantity'),
                    'type': upload_return.get('type'),
                    'form': form}
            except InvalidShapefileError as error:
                context = {
                    'uploaded': True,
                    'success': False,
                    'form': form,
                    'message': error.message}
        else:
            context = {'form': UploadFileForm()}
            return render(request, 'core/upload.html', context)
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
                msg = _('''Your account is not active. Please contact the
                        system administrator''')
                return redirect(reverse('core:login'))
        else:
            msg = _('Invalid username or password.')
            return render(request, 'core/login_page.html', {'msg': msg})

    return render(request, 'core/login_page.html', {'msg': msg})


def logout_view(request):
    logout(request)
    return redirect(reverse('core:index'))


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='core:login')


class EmbargoDetailView(LoginRequiredMixin, DetailView):
    model = EmbargoOEMA
    context_object_name = 'embargo'


class AutoInfracaoDetailView(LoginRequiredMixin, DetailView):
    model = AutoInfracaoOEMA
    context_object_name = 'infracao'


class UserUploads(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'core/user_uploads.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserUploads, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        return self.request.user


class AsvDetailView(LoginRequiredMixin, DetailView):
    model = Asv
    context_object_name = 'asv'


class AreaSolturaDetailView(LoginRequiredMixin, DetailView):
    model = AreaSoltura
    context_object_name = 'areasoltura'


class AsvMaDetailView(LoginRequiredMixin, DetailView):
    model = AsvMataAtlantica
    context_object_name = 'asvma'


class CompensacaoDetailView(LoginRequiredMixin, DetailView):
    model = CompensacaoMataAtlantica
    context_object_name = 'compensacao'


class CommonDeleteView(LoginRequiredMixin, DeleteView):

    def get_success_url(self):
        return reverse('core:user-uploads')

    def get_queryset(self):
        qs = super(CommonDeleteView, self).get_queryset()
        return qs.filter(usuario=self.request.user)


class AsvDeleteView(CommonDeleteView):
    model = Asv


class AsvMaDeleteView(CommonDeleteView):
    model = AsvMataAtlantica


class AreaSolturaDeleteView(CommonDeleteView):
    model = AreaSoltura


class CompensacaoDeleteView(CommonDeleteView):
    model = CompensacaoMataAtlantica


class EmbargoDeleteView(CommonDeleteView):
    model = EmbargoOEMA


class AutoInfracaoDeleteView(CommonDeleteView):
    model = AutoInfracaoOEMA


# GeoViews
class EmbargoGeoView(LoginRequiredMixin, RetrieveAPIView):
    queryset = EmbargoOEMA.objects.all()
    serializer_class = EmbargoSerializer


class AutoInfracaoGeoView(LoginRequiredMixin, RetrieveAPIView):
    queryset = AutoInfracaoOEMA.objects.all()
    serializer_class = AutoInfracaoSerializer


class AsvGeoView(LoginRequiredMixin, RetrieveAPIView):
    queryset = Asv.objects.all()
    serializer_class = AsvSerializer


class SolturaGeoView(LoginRequiredMixin, RetrieveAPIView):
    queryset = AreaSoltura.objects.all()
    serializer_class = SolturaSerializer


class AsvMaGeoView(LoginRequiredMixin, RetrieveAPIView):
    queryset = AsvMataAtlantica.objects.all()
    serializer_class = AsvMaSerializer


class CompensacaoGeoView(LoginRequiredMixin, RetrieveAPIView):
    queryset = CompensacaoMataAtlantica.objects.all()
    serializer_class = CompensacaoSerializer