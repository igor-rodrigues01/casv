# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .views import upload_file, logout_view, UserUploads
from .views import AsvDetailView, AsvDeleteView
from .views import CompensacaoDetailView, CompensacaoDeleteView
from .views import AreaSolturaDetailView, AreaSolturaDeleteView
from .views import AsvGeoView, SolturaGeoView, CompensacaoGeoView
from .views import EmbargoDetailView, EmbargoDeleteView
from .views import AutoInfracaoDetailView, AutoInfracaoDeleteView
from .views import EmbargoGeoView, AutoInfracaoGeoView,IbamaPedidoAnuenciaDetailView
from .views import IbamaAnuenciaListView,IbamaConcederAnuenciaView

from .views import DadosAnuenciaMaDetailView,DadosAnuenciaMaDeleteView
from .views import GeomPedidoAnuenciaMaGeoView,GeomAnuenciaConcedidaMaGeoView
from .views import IbamaAnuenciaConcedida,IbamaDadosAnuenciaConcedida
from .views import LoginView,DadosPedidoAnuenciaUsuarioMaView,IbamaDadosAnuenciaMaDeleteView
from .views import IbamaDownloadShpUser


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
    
    url(r'^download/shp_user/(?P<processo>\d+)/$',staff_member_required(IbamaDownloadShpUser.as_view()),name='shp-user'),

    url(r'^upload/',
        login_required(upload_file, login_url='/login/'),
        name='upload'),

    url(r'^file-models/',
        TemplateView.as_view(template_name='core/file-models.html'),
        name='file-models'),

    url(r'^login/', LoginView.as_view(), name='login'),

    url(r'^logout/', logout_view, name='logout'),

    url(r'^user-uploads/',
        UserUploads.as_view(),
        name='user-uploads'),

    url(r'^ibama/$',
        staff_member_required(IbamaAnuenciaListView.as_view(),
        login_url='/login/'),
        name='ibama-list'),
    
    url(r'^ibama/concessao/(?P<processo>\d+)/$',
        staff_member_required(IbamaConcederAnuenciaView.as_view(),
        login_url='/login/'),
        name='ibama-concessao'),

    url(r'^ibama/concedidos/$',
        staff_member_required(IbamaAnuenciaConcedida.as_view(),
        login_url='/login/'),
        name='ibama-concedidos'),

    url(r'^ibama/concedidos/(?P<processo>\d+)/$',
        staff_member_required(IbamaDadosAnuenciaConcedida.as_view(),
        login_url='/login/'),
        name='ibama-concedidos-dados'),

    url(r'^ibama/dados-pedido/(?P<processo>\d+)/$',
        staff_member_required(IbamaPedidoAnuenciaDetailView.as_view(),
        login_url='/login/'),
        name='ibama-geo'),

    url(r'^ibama/(?P<processo>\d+)/delete$',
        staff_member_required(IbamaDadosAnuenciaMaDeleteView.as_view(),
        login_url='/login/'),
        name='ibama-delete'),

    url(r'^asv/(?P<pk>\d+)/$',
        AsvDetailView.as_view(),
        name='asv'),

    url(r'^asv/(?P<pk>\d+)/delete/$',
        AsvDeleteView.as_view(),
        name='delete-asv'),

    url(r'^areasoltura/(?P<pk>\d+)/$',
        AreaSolturaDetailView.as_view(),
        name='areasoltura'),

    url(r'^areasoltura/(?P<pk>\d+)/delete/$',
        AreaSolturaDeleteView.as_view(),
        name='delete-areasoltura'),

    url(r'^pedido-anuencia/(?P<processo>\d+)/$',
        DadosPedidoAnuenciaUsuarioMaView.as_view(
        template_name = 'core/pedidoanuenciamataatlantica_detail.html'),
        name='pedido_anuencia'),

    url(r'^pedido-anuencia/(?P<pk>\d+)/delete/$',
        DadosAnuenciaMaDeleteView.as_view(
        template_name = 'core/pedidoanuenciamataatlantica_confirm_delete.html'),
        name='delete-pedido_anuencia'),

    url(r'^pedido-anuencia/geo/(?P<processo>\d+)/$',
        GeomPedidoAnuenciaMaGeoView.as_view(),
        name='geo-pedido_anuencia'),
    
    url(r'^anuencia-concedida/geo/(?P<processo>\d+)/$',
        GeomAnuenciaConcedidaMaGeoView.as_view(),
        name='geo-anuencia_concedida'),

    url(r'^compensacao/(?P<pk>\d+)/$',
        CompensacaoDetailView.as_view(),
        name='compensacao'),

    url(r'^compensacao/(?P<pk>\d+)/delete/$',
        CompensacaoDeleteView.as_view(),
        name='delete-compensacao'),

    url(r'^embargo/(?P<pk>\d+)/$',
        EmbargoDetailView.as_view(),
        name='embargo'),

    url(r'^embargo/(?P<pk>\d+)/delete/$',
        EmbargoDeleteView.as_view(),
        name='delete-embargo'),

    url(r'^infracao/(?P<pk>\d+)/$',
        AutoInfracaoDetailView.as_view(),
        name='infracao'),

    url(r'^infracao/(?P<pk>\d+)/delete/$',
        AutoInfracaoDeleteView.as_view(),
        name='delete-infracao'),

    url(r'^embargo/geo/(?P<pk>\d+)/$',
        EmbargoGeoView.as_view(),
        name='geo-embargo'),

    url(r'^infracao/geo/(?P<pk>\d+)/$',
        AutoInfracaoGeoView.as_view(),
        name='geo-infracao'),

    url(r'^compensacao/geo/(?P<pk>\d+)/$',
        CompensacaoGeoView.as_view(),
        name='geo-compensacao'),

    url(r'^asv/geo/(?P<pk>\d+)/$',
        AsvGeoView.as_view(),
        name='geo-asv'),

    url(r'^areasoltura/geo/(?P<pk>\d+)/$',
        SolturaGeoView.as_view(),
        name='geo-areasoltura'),
    
)