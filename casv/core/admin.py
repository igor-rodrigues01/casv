from django.contrib.gis import admin

from .models import Asv


class AsvAdmin(admin.OSMGeoAdmin):

    list_display = ['codigo', 'nom_prop', 'area_ha', 'municipio', 'uf',
        'usuario', 'data_criacao']
    list_filter = ['uf']
    search_fields = ['codigo', 'nom_prop', 'usuario', 'detentor', 'rt', 'municipio']


admin.site.register(Asv, AsvAdmin)