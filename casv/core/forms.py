# -*- coding: utf-8 -*-
from django import forms


class UploadFileForm(forms.Form):
    upload_file = forms.FileField()


class RegisterUserForm(forms.Form):

    email = forms.EmailField()