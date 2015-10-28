# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import upload_file, login_view, logout_view, UserUploads
from .views import AsvDetailView, AsvDeleteView
from .views import AsvMaDetailView
from .views import CompensacaoDetailView, AreaSolturaDetailView

from .views import CompensacaoGeoView, AsvMaGeoView, AsvGeoView, SolturaGeoView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
    url(r'^upload/',
        login_required(upload_file, login_url='/login/'),
        name='upload'),
    url(r'^file-models/',
        TemplateView.as_view(template_name='core/file-models.html'),
        name='file-models'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^user/(?P<pk>\d+)/uploads/$',
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
    url(r'^asvma/(?P<pk>\d+)/$',
        AsvMaDetailView.as_view(),
        name='asvma'),
    url(r'^compensacao/(?P<pk>\d+)/$',
        CompensacaoDetailView.as_view(),
        name='compensacao'),

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
)
