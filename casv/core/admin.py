from django.contrib.gis import admin

from .models import Asv, AreaSoltura, AsvMataAtlantica, CompensacaoMataAtlantica


class AsvAdmin(admin.OSMGeoAdmin):

    list_display = ['codigo', 'nom_prop', 'area_ha', 'municipio', 'uf',
        'usuario', 'data_criacao']
    list_filter = ['uf']
    search_fields = ['codigo', 'nom_prop', 'usuario', 'detentor', 'rt', 'municipio']


class AreaSolturaAdmin(admin.OSMGeoAdmin):

    list_display = ['processo', 'proprietario', 'data_criacao']
    list_filter = ['uf', 'data_criacao']
    search_fields = ['processo', 'proprietario']


class AsvMataAtlanticaAdmin(admin.OSMGeoAdmin):

    list_display = ['processo', 'empreendedor', 'municipio',
        'tipo_empreendimento', 'data_criacao']
    list_filter = ['uf', 'data_criacao', 'tipo_empreendimento']
    search_fields = ['processo', 'empreendedor', 'cpfj']


class CompensacaoMataAtlanticaAdmin(admin.OSMGeoAdmin):

    list_display = ['processo', 'empreendedor', 'municipio',
        'tipo_empreendimento',  'data_criacao']
    list_filter = ['uf', 'data_criacao', 'tipo_empreendimento']
    search_fields = ['processo', 'empreendedor', 'cpfj']


admin.site.register(Asv, AsvAdmin)
admin.site.register(AreaSoltura, AreaSolturaAdmin)
admin.site.register(AsvMataAtlantica, AsvMataAtlanticaAdmin)
admin.site.register(CompensacaoMataAtlantica, CompensacaoMataAtlanticaAdmin)