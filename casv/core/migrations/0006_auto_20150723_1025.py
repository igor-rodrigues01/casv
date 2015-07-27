# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20150720_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsvMataAtlantica',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('processo', models.IntegerField()),
                ('uf', models.CharField(verbose_name='Unidade da Federação', max_length=2)),
                ('municipio', models.CharField(verbose_name='Município', max_length=255)),
                ('empreendedor', models.CharField(max_length=255)),
                ('tipo_empreendimento', models.CharField(verbose_name='Tipo de Empreendimento', max_length=255)),
                ('cpfj', models.CharField(verbose_name='CPF ou CNPJ do Empreendedor', max_length=22, blank=True)),
                ('area_supressao_total', models.FloatField(verbose_name='Área Total de Supressão (ha)')),
                ('area_supressao_veg_primaria', models.FloatField(verbose_name='Área de Supressão de\n        Vegetação Primária (ha)')),
                ('area_supressao_estagio_medio', models.FloatField(verbose_name='Área de Supressão em\n        Estágio Médio (ha)')),
                ('area_supressao_estagio_avancado', models.FloatField(verbose_name='Área de Supressão em\n        Estágio Avançado (ha)')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4674)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompensacaoMataAtlantica',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('processo', models.IntegerField()),
                ('uf', models.CharField(verbose_name='Unidade da Federação', max_length=2)),
                ('municipio', models.CharField(verbose_name='Município', max_length=255)),
                ('empreendedor', models.CharField(max_length=255)),
                ('tipo_empreendimento', models.CharField(verbose_name='Tipo de Empreendimento', max_length=255)),
                ('cpfj', models.CharField(verbose_name='CPF ou CNPJ do Empreendedor', max_length=22, blank=True)),
                ('area_compensacao', models.FloatField(verbose_name='Área de Compensação (ha)')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4674)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='agua',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='carta',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='conectividade',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='conservacao',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='documento',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='mapa',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='reabilitador',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='uc',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='asv',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação'),
        ),
    ]
