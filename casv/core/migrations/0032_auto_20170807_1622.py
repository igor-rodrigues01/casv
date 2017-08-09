# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0031_auto_20170731_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosAnuenciaMataAtlantica',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('processo', models.IntegerField(blank=True, null=True, unique=True)),
                ('uf', models.CharField(blank=True, verbose_name='Unidade da Federação', null=True, max_length=2)),
                ('municipio', models.CharField(blank=True, verbose_name='Município', null=True, max_length=255)),
                ('empreendedor', models.CharField(blank=True, null=True, max_length=255)),
                ('tipo_empreendimento', models.CharField(blank=True, verbose_name='Tipo de Empreendimento', null=True, max_length=255)),
                ('cpfj', models.CharField(blank=True, verbose_name='CPF ou CNPJ do Empreendedor', null=True, max_length=22)),
                ('area_empreendimento_total', models.FloatField(blank=True, verbose_name='Área Total de Empreendimento (ha)', null=True)),
                ('area_empreendimento_veg_primaria', models.FloatField(blank=True, verbose_name='Área Empreendida em Vegetação Primária (ha)', null=True)),
                ('area_empreendimento_estagio_medio', models.FloatField(blank=True, verbose_name='Área de Empreendimento em Estágio Médio (ha)', null=True)),
                ('area_empreendimento_estagio_avancado', models.FloatField(blank=True, verbose_name='Área de Empreendimento em Estágio Avançado (ha)', null=True)),
                ('data_criacao', models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)),
                ('urbano_metropolitano', models.CharField(verbose_name='Local Urbarno', max_length=5)),
                ('status', models.CharField(verbose_name='Status', max_length=30)),
                ('observacao', models.TextField(blank=True, verbose_name='Observação', null=True)),
                ('usuario', models.ForeignKey(related_name='dadosanuencia', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Dados de Anuência - Mata Atlântica',
                'verbose_name': 'Dados de Anuência - Mata Atlântica',
            },
        ),
        migrations.CreateModel(
            name='GeomAnuenciaConcedidaMataAtlantica',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674)),
                ('processo', models.OneToOneField(db_column='processo', to_field='processo', to='core.DadosAnuenciaMataAtlantica')),
            ],
            options={
                'verbose_name_plural': 'Geometrias das Anuências Concedidas',
                'verbose_name': 'Geometria de Anuência Concedida - Mata Atlântica',
            },
        ),
        migrations.CreateModel(
            name='GeomPedidoAnuenciaMataAtlantica',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674)),
                ('processo', models.OneToOneField(db_column='processo', to_field='processo', to='core.DadosAnuenciaMataAtlantica')),
            ],
            options={
                'verbose_name_plural': 'Geometrias dos Pedidos de Anuência - Mata Atlântica',
                'verbose_name': 'Geometria do Pedido de Anuência - Mata Atlântica',
            },
        ),
        migrations.RemoveField(
            model_name='anuenciaconcedidamataatlantica',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='pedidoanuenciamataatlantica',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='AnuenciaConcedidaMataAtlantica',
        ),
        migrations.DeleteModel(
            name='PedidoAnuenciaMataAtlantica',
        ),
    ]
