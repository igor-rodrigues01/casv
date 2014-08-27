# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.gis.geos import Polygon
from django.contrib.auth.models import User

from ..models import Asv


class TestAsv(TestCase):
    def setUp(self):
        user = User.objects.create_superuser('user', 'i@t.com', 'password')
        self.asv = Asv.objects.create(code=1, area_ha=9.2, n_proc='abc12',
            reservator='yes', typology='abc12', user=user,
            polygon=Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
            )

    def test_asv_creation(self):
        self.assertTrue(isinstance(self.asv, Asv))
        self.assertEqual(self.asv.__str__(), self.asv.code)