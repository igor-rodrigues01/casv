from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Asv(models.Model):

    code = models.IntegerField(max_length=10)
    area_ha = models.FloatField()
    n_proc = models.CharField(max_length=19)
    reservator = models.CharField(max_length=3)
    typology = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    date = models.DateTimeField('Upload Date', auto_now_add=True)

    polygon = models.PolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.id