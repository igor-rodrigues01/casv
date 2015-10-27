# -*- coding: utf-8 -*-

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica


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



