# -*- coding: utf-8 -*-
from datetime import date

from django.test import TestCase
from django.contrib.gis.geos import Polygon
from django.contrib.auth.models import User

from ..models import Asv, AreaSoltura, AsvMataAtlantica
from ..models import CompensacaoMataAtlantica


class TestAsv(TestCase):
    def setUp(self):
        user = User.objects.create_user('user', 'i@t.com', 'password')
        self.asv = Asv.objects.create(
            codigo=1, n_autex=1837813, uf='BA', fito='teste', nom_prop='Maria',
            cpfj_prop='123.323.678/0001-23', detentor='João',
            cpfj_dete='123.456.789/0001-34', rt='Atenção',
            cpfj_rt='987.654.321/0001-23', area_ha=9.2, lenha_st=345.32,
            tora_m=23.32, torete_m=3435.23, mourao_m=3456.43,
            data_autex='2014-9-1', valido_ate='2015-1-1',
            municipio='Itacaré', usuario=user,
            geom=Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
            )

    def test_asv_creation(self):
        self.assertIsInstance(self.asv, Asv)
        self.assertEqual(self.asv.__str__(), "%s" % self.asv.codigo)
        self.assertEqual(
            Asv.objects.get(codigo=1).data_autex, date(2014, 9, 1)
            )


class TestAreaSoltura(TestCase):

    def setUp(self):
        user = User.objects.create_user('user', 'i@t.com', 'password')
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
            reabilitador=True,
            viveiros=99,
            distancia=87.9,
            tempo='09:21',
            taxon='Teste',
            vistoria=date(2015, 1, 1),
            usuario=user,
            geom=Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
        )

    def test_area_soltura_creation(self):
        self.assertEqual(AreaSoltura.objects.all().count(), 1)
        self.assertIsInstance(self.area_soltura, AreaSoltura)


class TestAsvMataAtlantica(TestCase):

    def setUp(self):
        user = User.objects.create_user('user', 'i@t.com', 'password')
        self.asv_mata_atlantica = AsvMataAtlantica.objects.create(
            processo=1,
            uf='BA',
            municipio='Itacaré',
            empreendedor='Teste',
            tipo_empreendimento='Fazenda',
            cpfj='123.323.678/0001-23',
            area_supressao_total=15.4,
            area_supressao_veg_primaria=1.4,
            area_supressao_estagio_medio=7.4,
            area_supressao_estagio_avancado=6.8,
            usuario=user,
            geom=Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
        )

    def test_asv_mata_atlantica_creation(self):
        self.assertEqual(AsvMataAtlantica.objects.all().count(), 1)
        self.assertIsInstance(self.asv_mata_atlantica, AsvMataAtlantica)


class TestCompensacaoMataAtlantica(TestCase):

    def setUp(self):
        user = User.objects.create_user('user', 'i@t.com', 'password')
        self.compensacao = CompensacaoMataAtlantica.objects.create(
            processo=1,
            uf='BA',
            municipio='Itacaré',
            empreendedor='Teste',
            tipo_empreendimento='Fazenda',
            cpfj='123.323.678/0001-23',
            area_compensacao=15.4,
            usuario=user,
            geom=Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
        )

        def test_asv_mata_atlantica_creation(self):
            self.assertEqual(CompensacaoMataAtlantica.objects.all().count(), 1)
            self.assertIsInstance(self.compensacao, CompensacaoMataAtlantica)