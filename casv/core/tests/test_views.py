# -*- coding: utf-8 -*-
from os.path import abspath
from datetime import date,datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.geos import Polygon,MultiPolygon

from ..models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica
from ..models import DadosAnuenciaMataAtlantica,GeomPedidoAnuenciaMataAtlantica,GeomAnuenciaConcedidaMataAtlantica
from ..models import GeomAnuenciaConcedidaMataAtlantica
from ..models import EmbargoOEMA, AutoInfracaoOEMA,LDAPUser,UserPermited
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
        self.user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')

    def test_unlogged_response(self):
        response = self.client.get(reverse('core:upload'))
        self.assertRedirects(response, reverse('core:login') + '?next=/upload/')

    def test_logged_response(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get(reverse('core:upload'))
        self.assertEqual(response.status_code, 302)


class HandleUploadedFileTest(TestCase):
    def setUp(self):
        self.user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
        self.asv_return = handle_uploaded_file(
            abspath('core/fixtures/Asv.zip'),
            self.user
        )
        self.area_soltura_return = handle_uploaded_file(
            abspath('core/fixtures/AreaSoltura.zip'),
            self.user
        )

        self.pedido_anuencia_return = handle_uploaded_file(
            abspath('core/fixtures/Pedido_Anuencia.zip'),
            self.user
        )
        
        self.compensacao_return = handle_uploaded_file(
            abspath('core/fixtures/CompensacaoMataAtlantica.zip'),
            self.user
        )
        self.embargo_return = handle_uploaded_file(
            abspath('core/fixtures/EmbargoOEMA.zip'),
            self.user
        )

        self.infracao_return = handle_uploaded_file(
            abspath('core/fixtures/AutoInfracaoOEMA.zip'),
            self.user
        )


    def test_import_asv(self):
        self.assertEqual(Asv.objects.all().count(), 2)
        asv = Asv.objects.create(codigo=1,geom=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))))
        self.assertTrue(asv)
        self.assertEqual(self.asv_return, {'type': 'Asv', 'quantity': 2})

    def test_import_area_soltura(self):
        self.assertEqual(AreaSoltura.objects.all().count(), 1)
        area_soltura = AreaSoltura.objects.all()[0]
        self.assertEqual(area_soltura.vistoria, date(2015, 1, 1))
        self.assertTrue(area_soltura.conservacao, True)
        self.assertEqual(area_soltura.usuario, self.user)
        self.assertEqual(self.area_soltura_return, {'type': 'AreaSoltura', 'quantity': 1})

    def test_import_pedido_anuencia(self):
        self.assertEqual(DadosAnuenciaMataAtlantica.objects.all().count(), 1)
        dados = DadosAnuenciaMataAtlantica.objects.all()[0]
        self.assertEqual(dados.municipio, 'Teste')
        self.assertEqual(dados.usuario, self.user)
        self.assertEqual(self.pedido_anuencia_return, {'type': 'GeomPedidoAnuenciaMataAtlantica',
            'quantity': 1})

    def test_import_compensacao(self):
        self.assertEqual(CompensacaoMataAtlantica.objects.all().count(), 1)
        compensacao = CompensacaoMataAtlantica.objects.all()[0]
        self.assertEqual(compensacao.municipio, 'Teste')
        self.assertEqual(compensacao.usuario, self.user)
        self.assertEqual(self.compensacao_return,
            {'type': 'CompensacaoMataAtlantica', 'quantity': 1})

    def test_import_embargo(self):
        self.assertEqual(EmbargoOEMA.objects.all().count(), 1)
        embargo = EmbargoOEMA.objects.all()[0]
        self.assertEqual(embargo.usuario, self.user)
        self.assertEqual(self.embargo_return, {
            'type': 'EmbargoOEMA',
            'quantity': 1
        })

    def test_import_auto_infracao(self):
        self.assertEqual(AutoInfracaoOEMA.objects.all().count(), 1)
        auto_infracao = AutoInfracaoOEMA.objects.all()[0]
        self.assertEqual(auto_infracao.usuario, self.user)
        self.assertEqual(self.infracao_return, {
            'type' : 'AutoInfracaoOEMA',
            'quantity' : 1
        })

    def test_wrong_shape(self):
        with self.assertRaises(InvalidShapefileError):
            handle_uploaded_file(
                abspath('core/fixtures/wrong-shape.zip'),
                self.user)
        with self.assertRaises(InvalidShapefileError):
            handle_uploaded_file(
                abspath('core/fixtures/ZipWithoutShp.zip'),
                self.user)
        with self.assertRaises(InvalidShapefileError):
            handle_uploaded_file(
                abspath('core/fixtures/AreaSoltura.shp'),
                self.user)


class LoginLogoutTest(TestCase):
    
    def setUp(self):
        self.ldap_username = 'ldap_username'
        self.ldap_password = 'ldap_password'

    def test_login_response(self):
        response = self.client.get(reverse('core:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_response(self):
        response = self.client.get(reverse('core:logout'))
        self.assertRedirects(response, reverse('core:index'))

    def test_loging_logout_user(self):

        self.client.post(
            reverse('core:login'),
            {'username':self.ldap_username, 'password':self.ldap_password})
        self.assertIn('_auth_user_id', self.client.session)
        self.client.get(reverse('core:logout'))
        self.assertNotIn('_auth_user_id', self.client.session)


class UserUploadsTest(TestCase):
    
    def setUp(self):
        self.user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')

    def test_user_uploads_unlogged_response(self):
        url = reverse('core:user-uploads')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_uploads_response(self):
      
        self.client.post(
            reverse('core:login'),
            {'username':self.user.username, 'password': self.user.password})
        url = reverse('core:user-uploads')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class UserUploadedFile(TestCase):

    def setUp(self):
        self.user = LDAPUser.objects.create_user('admin', 'password')
        self.ldap_username = 'ldap_username'
        self.ldap_password = 'ldap_password'

        self.asv_return = handle_uploaded_file(
            abspath('core/fixtures/Asv.zip'),
            self.user)

        self.area_soltura_return = handle_uploaded_file(
            abspath('core/fixtures/AreaSoltura.zip'),
            self.user)

        self.pedido_anuencia_return = handle_uploaded_file(
            abspath('core/fixtures/Pedido_Anuencia.zip'),
            self.user)

        self.compensacao_return = handle_uploaded_file(
            abspath('core/fixtures/CompensacaoMataAtlantica.zip'),
            self.user)

        self.embargo_return = handle_uploaded_file(
            abspath('core/fixtures/EmbargoOEMA.zip'),
            self.user)

        self.autoinfracao_return = handle_uploaded_file(
            abspath('core/fixtures/AutoInfracaoOEMA.zip'),
            self.user)


    def test_user_uploaded_asv_unlogged_response(self):
        pk = Asv.objects.all()[0].pk
        url = reverse('core:asv', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        url = reverse('core:geo-asv', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_uploaded_asv_response(self):
        
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password})
        pk = Asv.objects.all()[0].pk
        url = reverse('core:asv', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('core:geo-asv', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_uploaded_pedido_anuencia_response(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password})
        
        processo = DadosAnuenciaMataAtlantica.objects.all()[0].processo
        
        url      = reverse('core:pedido_anuencia', args=[processo])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        url = reverse('core:geo-pedido_anuencia', args=[processo])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_uploaded_pedido_anuencia_unlogged_response(self):
        processo = DadosAnuenciaMataAtlantica.objects.all()[0].processo
        
        url      = reverse('core:pedido_anuencia', args=[processo])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        
        url = reverse('core:geo-pedido_anuencia', args=[processo])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_uploaded_compensacao_unlogged_response(self):
        pk = CompensacaoMataAtlantica.objects.all()[0].pk
        url = reverse('core:compensacao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        url = reverse('core:geo-compensacao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_uploaded_compensacao_response(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password})
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
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password})
        pk = AreaSoltura.objects.all()[0].pk
        url = reverse('core:areasoltura', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('core:geo-areasoltura', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_uploaded_embargo_response(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password})
        pk = EmbargoOEMA.objects.all()[0].pk
        url = reverse('core:embargo', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('core:geo-embargo', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_uploaded_infracao_response(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password })
        pk = AutoInfracaoOEMA.objects.all()[0].pk
        url = reverse('core:infracao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('core:geo-infracao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestDeleteViews(TestCase):

    def setUp(self):
        # self.user2 = User.objects.create_user('user2', 'i@t.com', 'password')
        self.ldap_username = 'ldap_username'
        self.ldap_password = 'ldap_password'
        self.user = LDAPUser.objects.create_user(self.ldap_username,self.ldap_password)
        
        self.asv_return = handle_uploaded_file(
            abspath('core/fixtures/Asv.zip'),
            self.user)
        self.area_soltura_return = handle_uploaded_file(
            abspath('core/fixtures/AreaSoltura.zip'),
            self.user)

        self.compensacao_return = handle_uploaded_file(
            abspath('core/fixtures/CompensacaoMataAtlantica.zip'),
            self.user)
        self.embargo_return = handle_uploaded_file(
            abspath('core/fixtures/EmbargoOEMA.zip'),
            self.user)
        self.infracao_return = handle_uploaded_file(
            abspath('core/fixtures/AutoInfracaoOEMA.zip'),
            self.user)

    def test_asv_delete_view(self):
        self.assertEqual(Asv.objects.count(), 1)
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password})
        url = reverse('core:delete-asv', args=[Asv.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url)
        self.assertEqual(Asv.objects.count(), 0)

    def test_asv_delete_view_user_permission(self):
        self.client.post(
            reverse('core:login'),
            {'username': 'abc', 'password': 'abc'})
        url = reverse('core:delete-asv', args=[Asv.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_compensacao_delete_view(self):
        self.assertEqual(CompensacaoMataAtlantica.objects.count(), 1)
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password})
        url = reverse(
            'core:delete-compensacao',
            args=[CompensacaoMataAtlantica.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url)
        self.assertEqual(CompensacaoMataAtlantica.objects.count(), 0)

    def test_compensacao_delete_view_user_permission(self):
        self.client.post(
            reverse('core:login'),
            {'username': 'abc', 'password': 'abc'})
        url = reverse(
            'core:delete-compensacao',
            args=[CompensacaoMataAtlantica.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_areasoltura_delete_view(self):
        self.assertEqual(AreaSoltura.objects.count(), 1)
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password':self.ldap_password})
        url = reverse(
            'core:delete-areasoltura',
            args=[AreaSoltura.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url)
        self.assertEqual(AreaSoltura.objects.count(), 0)

    def test_areasoltura_delete_view_user_permission(self):
        self.client.post(
            reverse('core:login'),
            {'username': 'abc', 'password': 'password'})
        url = reverse(
            'core:delete-areasoltura',
            args=[AreaSoltura.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_embargooema_delete_view(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password': self.ldap_password })
        url = reverse(
            'core:delete-embargo',
            args=[EmbargoOEMA.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url)
        self.assertEqual(EmbargoOEMA.objects.count(), 0)

    def test_auto_infracao_delete_view(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.ldap_username, 'password':self.ldap_password})
        url = reverse(
            'core:delete-infracao',
            args=[AutoInfracaoOEMA.objects.all()[0].pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url)
        self.assertEqual(AutoInfracaoOEMA.objects.count(), 0)


class TestIbamaViews(TestCase):
    
    def setUp(self):
        LDAPUser.objects.create_user('ldap_username', 'ldap_password')

        try:
            self.user = 'ldap_username'
            self.password = 'ldap_password'
            print("\nTrying with ldap")
        except:

            self.user = 'admin'
            self.password = 'qwer1234'
            print("\nTrying with model backend")

        self.dados = DadosAnuenciaMataAtlantica.objects.create(
            processo=2,
            uf='df',
            municipio='teste',
            empreendedor='Emp test',
            tipo_empreendimento='Fazenda',
            cpfj='423423',
            area_empreendimento_total=3423,
            area_empreendimento_veg_primaria=432423,
            area_empreendimento_estagio_medio=234234,
            area_empreendimento_estagio_avancado=23423,
            usuario=LDAPUser.objects.all()[0],
            data_criacao=datetime.now(),
            data_modificacao_ibama=datetime.now(),
            cpf_modificacao_ibama='213213213',
            urbano_metropolitano='sim',
            status='EM análise',
            observacao='teste teste teste'
        )
    
    def test_ibama_conceder_anuencia_view(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.user,
             'password': self.password})

        pk  = DadosAnuenciaMataAtlantica.objects.all()[0].processo
        
        url = reverse('core:ibama-concessao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('core:ibama-geo', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ibama_conceder_anuencia_view_unlogged(self):
        pk  = DadosAnuenciaMataAtlantica.objects.all()[0].processo
        
        url = reverse('core:ibama-concessao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        url = reverse('core:ibama-geo', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


    def test_ibama_anuencia_concedida(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.user, 'password': self.password})

        response = self.client.get(reverse('core:ibama-concedidos'))
        self.assertEqual(response.status_code,200)

    def test_ibama_anuencia_concedida_unlogged(self):
        response = self.client.get(reverse('core:ibama-concedidos'))
        self.assertEqual(response.status_code,302)

    def test_ibama_dados_anuencia_concedida(self):
        self.client.post(reverse('core:login'),
            {'username': self.user, 'password': self.password})
       
        pk = DadosAnuenciaMataAtlantica.objects.all()[0].pk
        url = reverse('core:ibama-concessao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_ibama_dados_anuencia_concedida_unlogged(self):
        pk = DadosAnuenciaMataAtlantica.objects.all()[0].pk
        url = reverse('core:ibama-concessao', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)
 
    def test_ibama_anuencia_list_view(self):
        self.client.post(
            reverse('core:login'),
            {'username': self.user,
             'password': self.password})

        url = reverse('core:ibama-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_ibama_anuencia_list_view_unlogged_reponse(self):
        url = reverse('core:ibama-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

    def test_ibama_pedido_anuencia_detail_view(self):
        self.client.post(reverse('core:login'),
            {'username': self.user, 'password': self.password})
       
        pk = DadosAnuenciaMataAtlantica.objects.all()[0].processo
        url = reverse('core:ibama-geo', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_ibama_pedido_anuencia_detail_view_unlogged_response(self):  
        pk = DadosAnuenciaMataAtlantica.objects.all()[0].processo
        url = reverse('core:ibama-geo', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

    def test_ibama_dados_anuencia_ma_delete_view(self):
        self.client.post(reverse('core:login'),
            {'username': self.user, 'password': self.password})
       
        pk = DadosAnuenciaMataAtlantica.objects.all()[0].processo
        url = reverse('core:ibama-geo', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_ibama_dados_anuencia_ma_delete_view_unlogged_response(self):
        pk = DadosAnuenciaMataAtlantica.objects.all()[0].processo
        url = reverse('core:ibama-geo', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)
