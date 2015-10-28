# -*- coding: utf-8 -*-
from os.path import abspath
from datetime import date

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from ..models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica
from ..views import handle_uploaded_file, InvalidShapefileError


class IndexTest(TestCase):
    def test_index_response(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):
    def test_index_response(self):
        response = self.client.get(reverse('core:login'))
        self.assertEqual(response.status_code, 200)


class UploadTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')

    def test_unlogged_response(self):
        response = self.client.get(reverse('core:upload'))
        self.assertRedirects(response, reverse('core:login') + '?next=/upload/')

    def test_logged_response(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.get(reverse('core:upload'))
        self.assertEqual(response.status_code, 200)


class HandleUploadedFileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')
        self.asv_return = handle_uploaded_file(
            abspath('core/fixtures/Asv.zip'),
            self.user
            )
        self.area_soltura_return = handle_uploaded_file(
            abspath('core/fixtures/AreaSoltura.zip'),
            self.user
            )
        self.asvma_return = handle_uploaded_file(
            abspath('core/fixtures/AsvMataAtlantica.zip'),
            self.user
            )
        self.compensacao_return = handle_uploaded_file(
            abspath('core/fixtures/CompensacaoMataAtlantica.zip'),
            self.user
            )

    def test_import_asv(self):
        self.assertEqual(Asv.objects.all().count(), 1)
        asv = Asv.objects.get(codigo=1)
        self.assertEqual(asv.data_autex, date(2014, 9, 1))
        self.assertEqual(asv.valido_ate, date(2015, 1, 1))
        self.assertEqual(asv.usuario, self.user)
        self.assertEqual(self.asv_return, {'type': 'Asv', 'quantity': 1})

    def test_import_area_soltura(self):
        self.assertEqual(AreaSoltura.objects.all().count(), 1)
        area_soltura = AreaSoltura.objects.all()[0]
        self.assertEqual(area_soltura.vistoria, date(2015, 1, 1))
        self.assertTrue(area_soltura.conservacao, True)
        self.assertEqual(area_soltura.usuario, self.user)
        self.assertEqual(self.area_soltura_return, {'type': 'AreaSoltura', 'quantity': 1})

    def test_import_asvma(self):
        self.assertEqual(AsvMataAtlantica.objects.all().count(), 1)
        asvma = AsvMataAtlantica.objects.all()[0]
        self.assertEqual(asvma.municipio, 'Itacaré')
        self.assertEqual(asvma.area_supressao_total, 15.4)
        self.assertEqual(asvma.usuario, self.user)
        self.assertEqual(self.asvma_return, {'type': 'AsvMataAtlantica',
            'quantity': 1})

    def test_import_compensacao(self):
        self.assertEqual(CompensacaoMataAtlantica.objects.all().count(), 1)
        compensacao = CompensacaoMataAtlantica.objects.all()[0]
        self.assertEqual(compensacao.municipio, 'Itacaré')
        self.assertEqual(compensacao.area_compensacao, 15.4)
        self.assertEqual(compensacao.usuario, self.user)
        self.assertEqual(self.compensacao_return,
            {'type': 'CompensacaoMataAtlantica', 'quantity': 1})

    def test_wrong_shape(self):
        with self.assertRaises(InvalidShapefileError):
            handle_uploaded_file(
                abspath('core/fixtures/wrong-shape.zip'),
                self.user
            )
        with self.assertRaises(InvalidShapefileError):
            handle_uploaded_file(
                abspath('core/fixtures/ZipWithoutShp.zip'),
                self.user
            )
        with self.assertRaises(InvalidShapefileError):
            handle_uploaded_file(
                abspath('core/fixtures/AreaSoltura.shp'),
                self.user
            )


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
        url = reverse('core:user-uploads', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class UserUploadedFile(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')
        self.asv_return = handle_uploaded_file(
            abspath('core/fixtures/Asv.zip'),
            self.user
            )
        self.area_soltura_return = handle_uploaded_file(
            abspath('core/fixtures/AreaSoltura.zip'),
            self.user
            )
        self.asvma_return = handle_uploaded_file(
            abspath('core/fixtures/AsvMataAtlantica.zip'),
            self.user
            )
        self.compensacao_return = handle_uploaded_file(
            abspath('core/fixtures/CompensacaoMataAtlantica.zip'),
            self.user
            )

    def test_user_uploaded_asv_unlogged_response(self):
        pk = Asv.objects.all()[0].pk
        url = reverse('core:asv', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        url = reverse('core:geo-asv', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_uploaded_asv_response(self):
        self.client.post(reverse('core:login'),
            {'username': self.user.username, 'password': 'password'})
        pk = Asv.objects.all()[0].pk
        url = reverse('core:asv', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('core:geo-asv', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_uploaded_asvma_unlogged_response(self):
        pk = AsvMataAtlantica.objects.all()[0].pk
        url = reverse('core:asvma', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        url = reverse('core:geo-asvma', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_uploaded_asvma_response(self):
        self.client.post(reverse('core:login'),
            {'username': self.user.username, 'password': 'password'})
        pk = AsvMataAtlantica.objects.all()[0].pk
        url = reverse('core:asvma', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('core:geo-asvma', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_uploaded_compensacao_unlogged_response(self):
        pk = CompensacaoMataAtlantica.objects.all()[0].pk
        url = reverse('core:compensacao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        url = reverse('core:geo-compensacao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_uploaded_compensacao_response(self):
        self.client.post(reverse('core:login'),
            {'username': self.user.username, 'password': 'password'})
        pk = CompensacaoMataAtlantica.objects.all()[0].pk
        url = reverse('core:compensacao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('core:geo-compensacao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_uploaded_areasoltura_unlogged_response(self):
        pk = AreaSoltura.objects.all()[0].pk
        url = reverse('core:areasoltura', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        url = reverse('core:geo-areasoltura', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_uploaded_areasoltura_response(self):
        self.client.post(reverse('core:login'),
            {'username': self.user.username, 'password': 'password'})
        pk = AreaSoltura.objects.all()[0].pk
        url = reverse('core:areasoltura', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('core:geo-areasoltura', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestDeleteViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')
        self.asv_return = handle_uploaded_file(
            abspath('core/fixtures/Asv.zip'),
            self.user
            )
        self.area_soltura_return = handle_uploaded_file(
            abspath('core/fixtures/AreaSoltura.zip'),
            self.user
            )
        self.asvma_return = handle_uploaded_file(
            abspath('core/fixtures/AsvMataAtlantica.zip'),
            self.user
            )
        self.compensacao_return = handle_uploaded_file(
            abspath('core/fixtures/CompensacaoMataAtlantica.zip'),
            self.user
            )

    def test_asv_delete_view(self):
        self.assertEqual(Asv.objects.count(), 1)
        self.client.post(reverse('core:login'),
            {'username': self.user.username, 'password': 'password'})

        url = reverse('core:delete-asv', args=[Asv.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url)
        self.assertEqual(Asv.objects.count(), 0)