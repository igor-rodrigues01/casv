# -*- coding: utf-8 -*-
from os.path import abspath

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from ..models import Asv
from ..views import handle_uploaded_file


client = Client()
client2 = Client()


class IndexTest(TestCase):
    def test_index_response(self):
        response = client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)


class UploadTest(TestCase):
    def setUp(self):
        password = 'mypassword'
        user = User.objects.create_superuser('user', 'i@test.com', password)
        client2.login(username=user.username, password=password)

    def test_upload_response(self):
        response = client.get(reverse('core:upload'))
        self.assertEqual(response.status_code, 302)  # test without login
        logged_response = client2.get(reverse('core:upload'))
        self.assertEqual(logged_response.status_code, 200)  # test with login


class UploadSuccessTest(TestCase):
    def test_success_response(self):
        response = client.get(reverse('core:upload_success'))
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):
    def test_login_response(self):
        response = client.get(reverse('core:login'))
        self.assertEqual(response.status_code, 200)


class HandleUploadedFileTest(TestCase):
    def setUp(self):
        user = User.objects.create_superuser('user', 'i@test.com', 'mypassword')
        handle_uploaded_file(abspath('core/fixtures/test-import-shape.zip'), user)

    def test_import_shape(self):
        self.assertEqual(Asv.objects.all().count(), 1)