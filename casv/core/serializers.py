# -*- coding: utf-8 -*-

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica
from .models import (EmbargoOEMA, AutoInfracaoOEMA)
from .models import GeomPedidoAnuenciaMataAtlantica,GeomAnuenciaConcedidaMataAtlantica,DadosAnuenciaMataAtlantica


class AsvSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Asv
        id_field = False
        geo_field = 'geom'
        fields = []


class SolturaSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = AreaSoltura
        id_field = False
        geo_field = 'geom'
        fields = []


class AsvMaSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = AsvMataAtlantica
        id_field = False
        geo_field = 'geom'
        fields = []


class CompensacaoSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = CompensacaoMataAtlantica
        id_field = False
        geo_field = 'geom'
        fields = []


class EmbargoSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = EmbargoOEMA
        id_field = False
        fields = []
        geo_field = 'geom'


class AutoInfracaoSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = AutoInfracaoOEMA
        id_field = False
        fields = []
        geo_field = 'geom'


class GeomPedidoAnuenciaMaSerializer(GeoFeatureModelSerializer):
    
    class Meta:
        model     = GeomPedidoAnuenciaMataAtlantica
        id_field  = False
        fields    = []
        geo_field = 'geom'


class GeomAnuenciaConcedidaMaSerializer(GeoFeatureModelSerializer):
    
    class Meta:
        model     = GeomAnuenciaConcedidaMataAtlantica
        id_field  = False
        fields    = []
        geo_field = 'geom'
