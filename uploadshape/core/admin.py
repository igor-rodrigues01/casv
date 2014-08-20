from django.contrib.gis import admin

from .models import Shape


class ShapeAdmin(admin.OSMGeoAdmin):

    list_display = ['id', 'user', 'date']
    search_fields = ['id', 'user']


admin.site.register(Shape, ShapeAdmin)