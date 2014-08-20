# -*- coding: utf-8 -*-
from os.path import abspath

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from ..views import handle_uploaded_file
from ..models import Shape

client = Client()


class IndexTest(TestCase):
    def test_index_response(self):
        response = client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)


class UploadTest(TestCase):
    def test_upload_response(self):
        response = client.get(reverse('core:upload'))
        self.assertEqual(response.status_code, 200)


class UploadSuccessTest(TestCase):
    def test_success_response(self):
        response = client.get(reverse('core:upload_success'))
        self.assertEqual(response.status_code, 200)


class HandleUploadedFileTest(TestCase):

    def setUp(self):
        password = 'mypassword'
        user = User.objects.create_superuser('user', 'i@test.com', password)
        client.login(username=user.username, password=password)
        with open(abspath('core/fixtures/test-import-shape.zip')) as upload_file:
            client.post('/upload/', {'upload_file': upload_file})

    def test_import_shape(self):
        self.assertEqual(Shape.objects.all().count(), 85)