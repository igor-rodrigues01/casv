# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import upload_file


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
    url(r'^upload/',
        login_required(upload_file, login_url='/admin/'),
        name='upload'),
    url(r'^upload-success/', TemplateView.as_view(template_name='success.html'),
        name='upload_success'),
)