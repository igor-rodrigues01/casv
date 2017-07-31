from __future__ import absolute_import

from .base import *


DATABASES = {
    "default": {
        "ENGINE": 'django.contrib.gis.db.backends.postgis',
        "NAME": "test_upload",
        "USER": "test_upload",
        "PASSWORD": "test_upload",
        "HOST": "localhost",
        "PORT": "",
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

POSTGIS_VERSION = (2, 1, 3)

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
########## END EMAIL CONFIGURATION