from django.contrib.gis import admin

from .models import Asv


class AsvAdmin(admin.OSMGeoAdmin):

    list_display = ['id', 'user', 'date']
    search_fields = ['id', 'user']


admin.site.register(Asv, AsvAdmin)