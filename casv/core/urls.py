# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import upload_file, login_view, logout_view, UserUploads
from .views import AsvDetailView, AsvDeleteView
from .views import AsvMaDetailView, AsvMaDeleteView
from .views import CompensacaoDetailView, CompensacaoDeleteView
from .views import AreaSolturaDetailView, AreaSolturaDeleteView
from .views import AsvMaGeoView, AsvGeoView, SolturaGeoView, CompensacaoGeoView
from .views import EmbargoDetailView, EmbargoDeleteView
from .views import AutoInfracaoDetailView, AutoInfracaoDeleteView
from .views import EmbargoGeoView, AutoInfracaoGeoView

# ==============================
from .views import PedidoAnuenciaMa,PedidoAnuenciaMaDelete


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),

    url(r'^upload/',
        login_required(upload_file, login_url='/login/'),
        name='upload'),

    url(r'^file-models/',
        TemplateView.as_view(template_name='core/file-models.html'),
        name='file-models'),

    url(r'^login/', login_view, name='login'),

    url(r'^logout/', logout_view, name='logout'),

    url(r'^user-uploads/',
        UserUploads.as_view(),
        name='user-uploads'),

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

    url(r'^asvma/(?P<pk>\d+)/$',
        AsvMaDetailView.as_view(),
        name='asvma'),

    url(r'^asvma/(?P<pk>\d+)/delete/$',
        AsvMaDeleteView.as_view(),
        name='delete-asvma'),

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

    url(r'^asvma/geo/(?P<pk>\d+)/$',
        AsvMaGeoView.as_view(),
        name='geo-asvma'),

    url(r'^asv/geo/(?P<pk>\d+)/$',
        AsvGeoView.as_view(),
        name='geo-asv'),

    url(r'^areasoltura/geo/(?P<pk>\d+)/$',
        SolturaGeoView.as_view(),
        name='geo-areasoltura'),
    
    #==================
    url(r'^pedido-anuencia/(?P<pk>\d+)/$',
        PedidoAnuenciaMa.as_view(),name='pedido_anuencia'),

    url(r'^pedido-anuencia/(?P<pk>\d+)/delete/$',
    PedidoAnuenciaMaDelete.as_view(template_name='core/confirm_delete.html'),
    name='delete-pedido_anuencia')
    
    #================== 
)