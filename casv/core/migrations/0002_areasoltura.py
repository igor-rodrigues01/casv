# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSoltura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('processo', models.IntegerField()),
                ('nome', models.CharField(verbose_name='Nome da propriedade', max_length=255)),
                ('endereco', models.CharField(verbose_name='Endereço', max_length=400)),
                ('municipio', models.CharField(verbose_name='Município', max_length=255)),
                ('uf', models.CharField(verbose_name='Unidade da Federação', max_length=2)),
                ('proprietario', models.CharField(verbose_name='Nome do proprietário', max_length=255)),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('telefone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('area', models.FloatField(verbose_name='Área da Propriedade (ha)')),
                ('arl_app', models.FloatField(verbose_name='Área de reserva legal e proteção permanente')),
                ('bioma', models.CharField(verbose_name='Bioma', max_length=255)),
                ('fitofisionomia', models.CharField(max_length=255)),
                ('atividade', models.CharField(verbose_name='Atividade Econômica', max_length=255)),
                ('viveiro', models.IntegerField(verbose_name='Número de viveiros')),
                ('distancia', models.FloatField(verbose_name='Área da Propriedade (ha)')),
                ('tempo', models.FloatField(verbose_name='Tempo de viagem ao CETAS mais próximo')),
                ('vistoria', models.DateField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4674)),
            ],
        ),
    ]
