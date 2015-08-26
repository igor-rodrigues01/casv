# -*- coding: utf-8 -*-

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica


class AsvSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Asv
        geo_field = 'geom'


class SolturaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AreaSoltura
        geo_field = 'geom'


class AsvMaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AsvMataAtlantica
        geo_field = 'geom'


class CompensacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CompensacaoMataAtlantica
        geo_field = 'geom'



