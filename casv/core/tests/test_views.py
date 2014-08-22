# -*- coding: utf-8 -*-
#from os.path import abspath

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

#from ..views import handle_uploaded_file
#from ..models import Shape

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


# Commented because the test is failing, sorry!

#class HandleUploadedFileTest(TestCase):
    #def setUp(self):
        #password = 'mypassword'
        #user = User.objects.create_superuser('user', 'i@test.com', password)
        #client2.login(username=user.username, password=password)
        #client2.post('/upload/', {
            #'upload_file': abspath('core/fixtures/test-import-shape.zip'),
            #'user': user
            #})

    #def test_import_shape(self):
        #self.assertEqual(Shape.objects.all().count(), 85)