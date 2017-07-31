# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0016_auto_20151201_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoInfracaoOEMA',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('proc', models.CharField(blank=True, max_length=30, null=True)),
                ('num_ai', models.CharField(blank=True, max_length=20, null=True)),
                ('num_tei', models.CharField(blank=True, max_length=20, null=True)),
                ('area_ha', models.DecimalField(blank=True, max_digits=8, null=True, decimal_places=2)),
                ('desc', models.CharField(blank=True, max_length=2500, null=True)),
                ('legislacao', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('cpfj', models.CharField(blank=True, max_length=20, null=True)),
                ('municipio', models.CharField(blank=True, max_length=250, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(blank=True, srid=4674, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='infracao')),
            ],
            options={
                'verbose_name_plural': 'Autos de Infração OEMA',
                'verbose_name': 'Auto de Infração OEMA',
            },
        ),
        migrations.CreateModel(
            name='EmbargoOEMA',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('proc', models.CharField(blank=True, max_length=30, null=True)),
                ('num_ai', models.CharField(blank=True, max_length=20, null=True)),
                ('num_tei', models.CharField(blank=True, max_length=20, null=True)),
                ('area_ha', models.DecimalField(blank=True, max_digits=8, null=True, decimal_places=2)),
                ('desc', models.CharField(blank=True, max_length=2500, null=True)),
                ('legislacao', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('cpfj', models.CharField(blank=True, max_length=20, null=True)),
                ('municipio', models.CharField(blank=True, max_length=250, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(blank=True, srid=4674, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='embargo')),
            ],
            options={
                'verbose_name_plural': 'Embargos OEMA',
                'verbose_name': 'Embargo OEMA',
            },
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='area_supressao_estagio_avancado',
            field=models.FloatField(blank=True, null=True, verbose_name='Área de Supressão em Estágio Avançado (ha)'),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='area_supressao_estagio_medio',
            field=models.FloatField(blank=True, null=True, verbose_name='Área de Supressão em Estágio Médio (ha)'),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='area_supressao_veg_primaria',
            field=models.FloatField(blank=True, null=True, verbose_name='Área de Supressão de Vegetação Primária (ha)'),
        ),
    ]
