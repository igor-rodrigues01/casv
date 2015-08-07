# -*- coding: utf-8 -*-
from os.path import abspath
from datetime import date

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from ..models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica
from ..views import handle_uploaded_file


class IndexTest(TestCase):
    def test_index_response(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)


class UploadTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')

    def test_unlogged_response(self):
        response = self.client.get(reverse('core:upload'))
        self.assertRedirects(response, '/login/?next=/upload/')

    def test_logged_response(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.get(reverse('core:upload'))
        self.assertEqual(response.status_code, 200)


class HandleUploadedFileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')
        handle_uploaded_file(
            abspath('core/fixtures/Asv.zip'),
            self.user
            )
        handle_uploaded_file(
            abspath('core/fixtures/AreaSoltura.zip'),
            self.user
            )
        handle_uploaded_file(
            abspath('core/fixtures/AsvMataAtlantica.zip'),
            self.user
            )
        handle_uploaded_file(
            abspath('core/fixtures/CompensacaoMataAtlantica.zip'),
            self.user
            )

    def test_import_asv(self):
        self.assertEqual(Asv.objects.all().count(), 1)
        asv = Asv.objects.get(codigo=1)
        self.assertEqual(asv.data_autex, date(2014, 9, 1))
        self.assertEqual(asv.valido_ate, date(2015, 1, 1))
        self.assertEqual(asv.usuario, self.user)

    def test_import_area_soltura(self):
        self.assertEqual(AreaSoltura.objects.all().count(), 1)
        area_soltura = AreaSoltura.objects.all()[0]
        self.assertEqual(area_soltura.vistoria, date(2015, 1, 1))
        self.assertTrue(area_soltura.conservacao, True)
        self.assertEqual(area_soltura.usuario, self.user)

    def test_import_asvma(self):
        self.assertEqual(AsvMataAtlantica.objects.all().count(), 1)
        asvma = AsvMataAtlantica.objects.all()[0]
        self.assertEqual(asvma.municipio, 'Itacaré')
        self.assertEqual(asvma.area_supressao_total, 15.4)
        self.assertEqual(asvma.usuario, self.user)

    def test_import_compensacao(self):
        self.assertEqual(CompensacaoMataAtlantica.objects.all().count(), 1)
        compensacao = CompensacaoMataAtlantica.objects.all()[0]
        self.assertEqual(compensacao.municipio, 'Itacaré')
        self.assertEqual(compensacao.area_compensacao, 15.4)
        self.assertEqual(compensacao.usuario, self.user)


class UploadSuccessTest(TestCase):
    def test_success_response(self):
        response = self.client.get(reverse('core:upload_success'))
        self.assertEqual(response.status_code, 200)


class LoginLogoutTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')

    def test_login_response(self):
        response = self.client.get(reverse('core:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_response(self):
        response = self.client.get(reverse('core:logout'))
        self.assertRedirects(response, reverse('core:index'))

    def test_loging_logout_user(self):
        self.client.post(reverse('core:login'),
            {'username': self.user.username, 'password': 'password'})
        self.assertIn('_auth_user_id', self.client.session)

        self.client.get(reverse('core:logout'))
        self.assertNotIn('_auth_user_id', self.client.session)


class UserUploadsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')

    def test_user_uploads_response(self):
        response = self.client.get('/user/%s/uploads/' % self.user.pk)
        self.assertEqual(response.status_code, 200)