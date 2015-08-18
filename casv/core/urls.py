# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import upload_file, login_view, logout_view, UserUploads
from .views import AsvDetailView, AsvMaDetailView
from .views import CompensacaoDetailView, AreaSolturaDetailView


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
    url(r'^areasoltura/(?P<pk>\d+)/$',
        AreaSolturaDetailView.as_view(),
        name='areasoltura'),
    url(r'^asvma/(?P<pk>\d+)/$',
        AsvMaDetailView.as_view(),
        name='asvma'),
    url(r'^compensacao/(?P<pk>\d+)/$',
        CompensacaoDetailView.as_view(),
        name='compensacao'),
)
