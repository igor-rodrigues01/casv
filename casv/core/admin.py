from django.contrib.gis import admin

from .models import Asv


class AsvAdmin(admin.OSMGeoAdmin):

    list_display = ['code', 'nom_prop', 'area_ha', 'municipio', 'uf',
        'user', 'date']
    list_filter = ['uf']
    search_fields = ['code', 'nom_prop', 'user', 'detentor', 'rt', 'municipio']


admin.site.register(Asv, AsvAdmin)