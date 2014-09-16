# -*- coding: utf-8 -*-
from datetime import date

from django.test import TestCase
from django.contrib.gis.geos import Polygon
from django.contrib.auth.models import User

from ..models import Asv


class TestAsv(TestCase):
    def setUp(self):
        user = User.objects.create_superuser('user', 'i@t.com', 'password')
        self.asv = Asv.objects.create(
            code=1, n_autex=1837813, uf='BA', fito='teste', nom_prop='Maria',
            cpfj_prop='123.323.678/0001-23', detentor='João',
            cpfj_dete='123.456.789/0001-34', rt='Atenção',
            cpfj_rt='987.654.321/0001-23', area_ha=9.2, lenha_st=345.32,
            tora_m=23.32, torete_m=3435.23, mourao_m=3456.43,
            data_autex='2014-9-1', valido_ate='2015-1-1',
            municipio='Itacaré', user=user,
            polygon=Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
            )

    def test_asv_creation(self):
        self.assertIsInstance(self.asv, Asv)
        self.assertEqual(self.asv.__str__(), "%s" % self.asv.code)
        self.assertEqual(
            Asv.objects.get(code=1).data_autex, date(2014, 9, 1)
            )