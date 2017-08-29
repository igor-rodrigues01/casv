# -*- coding: utf-8 -*-
from datetime import date,datetime

from django.test import TestCase
from django.contrib.gis.geos import Polygon,MultiPolygon
from django.contrib.auth.models import User

from ..models import Asv, AreaSoltura, AutoInfracaoOEMA
from ..models import EmbargoOEMA, CompensacaoMataAtlantica, LDAPUser
from ..models import DadosAnuenciaMataAtlantica,GeomPedidoAnuenciaMataAtlantica
from ..models import GeomAnuenciaConcedidaMataAtlantica


class TestAsv(TestCase):
    def setUp(self):
        user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
        self.asv = Asv.objects.create(
            codigo=1, n_autex=1837813, uf='BA', fito='teste', nom_prop='Maria',
            cpfj_prop='123.323.678/0001-23', detentor='João',
            cpfj_dete='123.456.789/0001-34', rt='Atenção',
            cpfj_rt='987.654.321/0001-23', area_ha=9.2, lenha_st=345.32,
            tora_m=23.32, torete_m=3435.23, mourao_m=3456.43,
            data_autex='2014-9-1', valido_ate='2015-1-1',
            municipio='Itacaré', usuario=user,
            geom=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))
        )

    def test_asv_creation(self):
        self.assertIsInstance(self.asv, Asv)
        self.assertEqual(self.asv.__str__(), "%s" % self.asv.codigo)
        self.assertEqual(
            Asv.objects.get(codigo=1).data_autex, date(2014, 9, 1)
        )


class TestAreaSoltura(TestCase):

    def setUp(self):
        user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
        self.area_soltura = AreaSoltura.objects.create(
            processo=1,
            nome='Fazenda Teste',
            uf='BA',
            municipio='Brumado',
            endereco='Rua Z',
            proprietario='Teste',
            cpf='12345678900',
            telefone='1234567890',
            email='teste@teste.org',
            area=5.6,
            arl_app=10.2,
            bioma='Caatinga',
            fitofisionomia='Fitofisionomia',
            conservacao=True,
            conectividade=True,
            uc=True,
            agua=True,
            atividade='Agricultura',
            documento=True,
            mapa=True,
            carta=True,
            distancia=87.9,
            vistoria=date(2015, 1, 1),
            usuario=user,
            geom=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))
        )

    def test_area_soltura_creation(self):
        self.assertEqual(AreaSoltura.objects.all().count(), 1)
        self.assertIsInstance(self.area_soltura, AreaSoltura)


class TestEmbargoOEMA(TestCase):

    def setUp(self):
        user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
        self.embargo = EmbargoOEMA.objects.create(
            proc='Teste',
            num_ai='0000000001',
            num_tei='0000000002',
            area_ha=100000.99,
            desc='Testando',
            legislacao='Teste',
            status='Teste 01',
            nome='Empresa teste',
            cpfj='123.323.678/0001-23',
            municipio='',
            usuario=user,
            geom=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))
        )

    def test_embargo_creation(self):
        self.assertEqual(EmbargoOEMA.objects.all().count(), 1)
        self.assertIsInstance(self.embargo, EmbargoOEMA)


class TestAutoInfracaoOEMA(TestCase):

    def setUp(self):
        user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
        self.autoinfracao = AutoInfracaoOEMA.objects.create(
            proc='Teste',
            num_ai='0000000001',
            num_tei='0000000002',
            area_ha=100000.99,
            desc='Testando',
            legislacao='Teste',
            status='Teste 01',
            nome='Empresa teste',
            cpfj='123.323.678/0001-23',
            municipio='',
            usuario=user,
            geom=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))
        )

    def test_auto_infracao_creation(self):
        self.assertEqual(AutoInfracaoOEMA.objects.all().count(), 1)
        self.assertIsInstance(self.autoinfracao, AutoInfracaoOEMA)


class TestCompensacaoMataAtlantica(TestCase):

    def setUp(self):
        ser = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
        self.compensacao, created = CompensacaoMataAtlantica.objects.get_or_create(
            processo=1,
            uf='BA',
            municipio='Itacaré',
            empreendedor='Teste',
            tipo_empreendimento='Fazenda',
            cpfj='123.323.678/0001-23',
            area_compensacao=15.4,
            usuario=user,
            geom=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))
        )

        def test_asv_mata_atlantica_creation(self):
            self.assertEqual(CompensacaoMataAtlantica.objects.count(), 1)
            self.assertEqual(self.compensacao.user, ser)
            self.assertIsInstance(self.compensacao, CompensacaoMataAtlantica)


class TestDadosAnuenciaMataAtlantica(TestCase):
    
    def setUp(self):
        user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
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
            usuario=user,
            data_criacao=datetime.now(),
            data_modificacao_ibama=datetime.now(),
            cpf_modificacao_ibama='213213213',
            urbano_metropolitano='sim',
            status='EM análise',
            observacao='teste teste teste'
        )

    def test_dados_anuencia_mata_atlantica(self):
        self.assertEqual(DadosAnuenciaMataAtlantica.objects.all().count(), 1)
        self.assertIsInstance(self.dados, DadosAnuenciaMataAtlantica)


class TestGeomPedidoAnuenciaMataAtlantica(TestCase):
    
    def setUp(self):
        user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
        self.model_geom = GeomPedidoAnuenciaMataAtlantica.objects.create(
            processo=DadosAnuenciaMataAtlantica.objects.create(processo=1),
            geom=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))),
            usuario=user,
            area_ha=1234.56
        )

    def test_geom_pedido_anuencia_mata_atlantica(self):
        self.assertEqual(GeomPedidoAnuenciaMataAtlantica.objects.all().count(), 1)
        self.assertIsInstance(self.model_geom, GeomPedidoAnuenciaMataAtlantica)


class TestGeomAnuenciaConcedidaMataAtlantica(TestCase):
    
    def setUp(self):
        user = LDAPUser.objects.create_user('ldap_username', 'ldap_password')
        self.model_geom = GeomAnuenciaConcedidaMataAtlantica.objects.create(
            processo=DadosAnuenciaMataAtlantica.objects.create(processo=1),
            geom=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))),
            usuario=user,
            area_ha=1234.56,
            data_criacao=datetime.now(),
        )

    def test_geom_anuencia_concedida_mata_atlantica(self):
        self.assertEqual(GeomAnuenciaConcedidaMataAtlantica.objects.all().count(), 1)
        self.assertIsInstance(self.model_geom, GeomAnuenciaConcedidaMataAtlantica)
        

