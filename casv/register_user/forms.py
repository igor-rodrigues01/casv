# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _


class RegisterForm(forms.Form):
    email = forms.EmailField(label=_('Email'))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    first_name = forms.CharField(label=_('First name'), max_length=30, required=False)
    last_name = forms.CharField(label=_('Last name'), max_length=30, required=False)
