from django.contrib.gis import admin

from .models import Asv


class AsvAdmin(admin.OSMGeoAdmin):

    list_display = ['code', 'area_ha', 'n_proc', 'reservator', 'typology',
        'user', 'date']
    search_fields = ['code', 'n_proc', 'user']


admin.site.register(Asv, AsvAdmin)