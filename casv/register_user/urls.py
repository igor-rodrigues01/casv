# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import register_user

urlpatterns = patterns('',
    url(r'^register/', register_user, name='register'),
)