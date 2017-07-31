# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asv',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('codigo', models.IntegerField(null=True)),
                ('n_autex', models.CharField(max_length=30, blank=True, verbose_name='Número de Autorização de Extração')),
                ('uf', models.CharField(max_length=2, blank=True, verbose_name='UF')),
                ('fito', models.CharField(max_length=60, blank=True)),
                ('nom_prop', models.CharField(max_length=60, blank=True, verbose_name='Nome do Proprietário')),
                ('cpfj_prop', models.CharField(max_length=22, blank=True, verbose_name='CPF ou CNPJ do Proprietário')),
                ('detentor', models.CharField(max_length=60, blank=True, verbose_name='Nome do Detentor')),
                ('cpfj_dete', models.CharField(max_length=22, blank=True, verbose_name='CPF ou CNPJ do Detentor')),
                ('rt', models.CharField(max_length=60, blank=True)),
                ('cpfj_rt', models.CharField(max_length=22, blank=True)),
                ('area_ha', models.FloatField(null=True)),
                ('lenha_st', models.FloatField(null=True)),
                ('tora_m', models.FloatField(null=True)),
                ('torete_m', models.FloatField(null=True)),
                ('mourao_m', models.FloatField(null=True)),
                ('data_autex', models.DateField(null=True, verbose_name='Data de Autorização de Extração')),
                ('valido_ate', models.DateField(null=True, verbose_name='Data de Validade da Autorização')),
                ('municipio', models.CharField(max_length=40, blank=True, verbose_name='Município')),
                ('upload_date', models.DateTimeField(verbose_name='Upload Date', auto_now_add=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4674)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
