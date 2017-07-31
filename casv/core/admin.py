from django.contrib.gis import admin

from .models import (Asv, AreaSoltura, AsvMataAtlantica,CompensacaoMataAtlantica,
AnuenciaConcedidaMataAtlantica,PedidoAnuenciaMataAtlantica,)
from .models import EmbargoOEMA, AutoInfracaoOEMA


class AutoInfracaoAdmin(admin.OSMGeoAdmin):

    list_display = ['proc', 'nome', 'data_criacao', 'legislacao', 'usuario']
    list_filter = ['municipio']
    search_fields = ['proc', 'nome', 'data_criacao', 'legislacao', 'usuario']


class EmbargoAdmin(admin.OSMGeoAdmin):

    list_display = ['proc', 'nome', 'data_criacao', 'legislacao', 'usuario']
    list_filter = ['municipio']
    search_fields = ['proc', 'nome', 'data_criacao', 'legislacao', 'usuario']


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


class PedidoAnuenciaMataAtlanticaAdmin(admin.OSMGeoAdmin):
    
    list_display = ['processo', 'empreendedor', 'municipio',
        'tipo_empreendimento',  'data_criacao','urbano_metropolitano','observacao']
    list_filter = ['uf', 'data_criacao', 'tipo_empreendimento']
    search_fields = ['processo', 'empreendedor', 'cpfj']


class AnuenciaConcedidaMataAtlanticaAdmin(admin.OSMGeoAdmin):
    
    list_display = ['processo', 'empreendedor', 'municipio',
        'tipo_empreendimento',  'data_criacao']
    list_filter = ['uf', 'data_criacao', 'tipo_empreendimento']
    search_fields = ['processo', 'empreendedor', 'cpf_cnpj']


admin.site.register(Asv, AsvAdmin)
admin.site.register(EmbargoOEMA, EmbargoAdmin)
admin.site.register(AutoInfracaoOEMA, AutoInfracaoAdmin)
admin.site.register(AreaSoltura, AreaSolturaAdmin)
admin.site.register(AsvMataAtlantica)
admin.site.register(CompensacaoMataAtlantica, CompensacaoMataAtlanticaAdmin)
admin.site.register(PedidoAnuenciaMataAtlantica,PedidoAnuenciaMataAtlanticaAdmin)
admin.site.register(AnuenciaConcedidaMataAtlantica,
    AnuenciaConcedidaMataAtlanticaAdmin)
