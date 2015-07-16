# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class Asv(models.Model):

    codigo = models.IntegerField(null=True)
    n_autex = models.CharField('Número de Autorização de Extração',
        max_length=30, blank=True)
    uf = models.CharField('UF', max_length=2, blank=True)
    fito = models.CharField(max_length=60, blank=True)
    nom_prop = models.CharField('Nome do Proprietário',
        max_length=60, blank=True)
    cpfj_prop = models.CharField('CPF ou CNPJ do Proprietário',
        max_length=22, blank=True)
    detentor = models.CharField('Nome do Detentor', max_length=60, blank=True)
    cpfj_dete = models.CharField('CPF ou CNPJ do Detentor',
        max_length=22, blank=True)
    rt = models.CharField(max_length=60, blank=True)
    cpfj_rt = models.CharField(max_length=22, blank=True)
    area_ha = models.FloatField(null=True)
    lenha_st = models.FloatField(null=True)
    tora_m = models.FloatField(null=True)
    torete_m = models.FloatField(null=True)
    mourao_m = models.FloatField(null=True)
    data_autex = models.DateField('Data de Autorização de Extração', null=True)
    valido_ate = models.DateField('Data de Validade da Autorização', null=True)
    municipio = models.CharField('Município', max_length=40, blank=True)

    user = models.ForeignKey(User)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)

    geom = models.PolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.codigo