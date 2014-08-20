from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Shape(models.Model):

    polygon = models.PolygonField(srid=4674)
    user = models.ForeignKey(User)
    date = models.DateTimeField('Upload Date', auto_now_add=True)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.id