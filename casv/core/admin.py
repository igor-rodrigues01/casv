from django.contrib.gis import admin

from .models import (Asv, AreaSoltura, AsvMataAtlantica,CompensacaoMataAtlantica,
GeomPedidoAnuenciaMataAtlantica,GeomAnuenciaConcedidaMataAtlantica,
DadosAnuenciaMataAtlantica)
from .models import EmbargoOEMA, AutoInfracaoOEMA
from .models import LDAPUser,UserPermited


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


class GeomPedidoAnuenciaMataAtlanticaAdmin(admin.OSMGeoAdmin):
    
    list_display  = ['processo','geom','area_ha']
    list_filter   = ['processo']
    search_fields = ['processo']


class GeomAnuenciaConcedidaMataAtlanticaAdmin(admin.OSMGeoAdmin):

    list_display  = ['processo','geom','area_ha','data_criacao']
    list_filter   = ['processo']
    search_fields = ['processo']


class DadosAnuenciaMataAtlanticaAdmin(admin.OSMGeoAdmin):

    list_display = ['processo','usuario' ,'empreendedor', 'municipio',
        'tipo_empreendimento',  'data_criacao','urbano_metropolitano',
        'status','observacao','ativo','data_modificacao_ibama',
        'cpf_modificacao_ibama']
    list_filter = ['uf', 'data_criacao', 'tipo_empreendimento','data_criacao']
    search_fields = ['processo', 'empreendedor', 'cpfj']


class LDAPUserAdmin(admin.OSMGeoAdmin):
    list_display  = ['name']
    search_fields = ['name']


class UserPermitedAdmin(admin.OSMGeoAdmin):
    list_display  = ['username']
    search_fields = ['username']

admin.site.register(Asv, AsvAdmin)
admin.site.register(EmbargoOEMA, EmbargoAdmin)
admin.site.register(AutoInfracaoOEMA, AutoInfracaoAdmin)
admin.site.register(AreaSoltura, AreaSolturaAdmin)
admin.site.register(AsvMataAtlantica)
admin.site.register(CompensacaoMataAtlantica, CompensacaoMataAtlanticaAdmin)
admin.site.register(GeomPedidoAnuenciaMataAtlantica,
    GeomPedidoAnuenciaMataAtlanticaAdmin)
admin.site.register(GeomAnuenciaConcedidaMataAtlantica,
    GeomAnuenciaConcedidaMataAtlanticaAdmin)
admin.site.register(DadosAnuenciaMataAtlantica,DadosAnuenciaMataAtlanticaAdmin)
admin.site.register(LDAPUser,LDAPUserAdmin)
admin.site.register(UserPermited,UserPermitedAdmin)