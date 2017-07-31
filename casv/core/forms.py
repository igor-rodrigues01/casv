# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _


class UploadFileForm(forms.Form):
    upload_file = forms.FileField(label=_('Upload file'))