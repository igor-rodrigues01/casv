# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import upload_file, login_view, logout_view, UserUploads


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
    url(r'^upload/',
        login_required(upload_file, login_url='/login/'),
        name='upload'),
    url(r'^file-models/',
        TemplateView.as_view(template_name='file-models.html'),
        name='file-models'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^user/(?P<pk>\d+)/uploads/$',
        UserUploads.as_view(),
        name='user-uploads'),
)
