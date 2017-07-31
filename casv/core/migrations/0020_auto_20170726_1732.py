# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0019_auto_20170726_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnuenciaConcedidaMataAtlantica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('processo', models.IntegerField(blank=True, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='Unidade da Federação')),
                ('municipio', models.CharField(blank=True, max_length=255, null=True, verbose_name='Município')),
                ('empreendedor', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_empreendimento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tipo de Empreendimento')),
                ('cpfj', models.CharField(blank=True, max_length=22, null=True, verbose_name='CPF ou CNPJ do Empreendedor')),
                ('area_supressao_total', models.FloatField(blank=True, verbose_name='Área Total de Supressão (ha)', null=True)),
                ('area_supressao_veg_primaria', models.FloatField(blank=True, verbose_name='Área de Supressão de Vegetação Primária (ha)', null=True)),
                ('area_supressao_estagio_medio', models.FloatField(blank=True, verbose_name='Área de Supressão em Estágio Médio (ha)', null=True)),
                ('area_supressao_estagio_avancado', models.FloatField(blank=True, verbose_name='Área de Supressão em Estágio Avançado (ha)', null=True)),
                ('data_criacao', models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674)),
                ('urbano_metropolitano', models.BooleanField(verbose_name='Local Urbarno')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações', null=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='anuconcedmat')),
            ],
            options={
                'verbose_name_plural': 'Anuências Concedidas -\n            Mata Atlântica',
                'verbose_name': 'Anuência Concedida - Mata Atlântica',
            },
        ),
        migrations.CreateModel(
            name='PedidoAnuenciaMataAtlantica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('processo', models.IntegerField(blank=True, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='Unidade da Federação')),
                ('municipio', models.CharField(blank=True, max_length=255, null=True, verbose_name='Município')),
                ('empreendedor', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_empreendimento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tipo de Empreendimento')),
                ('cpfj', models.CharField(blank=True, max_length=22, null=True, verbose_name='CPF ou CNPJ do Empreendedor')),
                ('area_supressao_total', models.FloatField(blank=True, verbose_name='Área Total de Supressão (ha)', null=True)),
                ('area_supressao_veg_primaria', models.FloatField(blank=True, verbose_name='Área de Supressão de Vegetação Primária (ha)', null=True)),
                ('area_supressao_estagio_medio', models.FloatField(blank=True, verbose_name='Área de Supressão em Estágio Médio (ha)', null=True)),
                ('area_supressao_estagio_avancado', models.FloatField(blank=True, verbose_name='Área de Supressão em Estágio Avançado (ha)', null=True)),
                ('data_criacao', models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674)),
                ('urbano_metropolitano', models.BooleanField(verbose_name='Local Urbarno')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações', null=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='pedanudmat')),
            ],
            options={
                'verbose_name_plural': ' Pedidos de Anuência -\n            Mata Atlântica',
                'verbose_name': 'Pedido de Anuência - Mata Atlântica',
            },
        ),
        migrations.RemoveField(
            model_name='compensacaomataatlantica',
            name='c_est_avan',
        ),
        migrations.RemoveField(
            model_name='compensacaomataatlantica',
            name='c_est_inic',
        ),
        migrations.RemoveField(
            model_name='compensacaomataatlantica',
            name='c_est_medi',
        ),
        migrations.RemoveField(
            model_name='compensacaomataatlantica',
            name='c_veg_prim',
        ),
        migrations.RemoveField(
            model_name='compensacaomataatlantica',
            name='obs',
        ),
        migrations.RemoveField(
            model_name='compensacaomataatlantica',
            name='tipo_compensacao',
        ),
        migrations.AddField(
            model_name='asvmataatlantica',
            name='compensacao_estagio_avan',
            field=models.FloatField(blank=True, verbose_name='Área de Compensação de Estágio Avançado (ha)', null=True),
        ),
        migrations.AddField(
            model_name='asvmataatlantica',
            name='compensacao_estagio_inic',
            field=models.FloatField(blank=True, verbose_name='Área de Compensação de Estágio Inicial (ha)', null=True),
        ),
        migrations.AddField(
            model_name='asvmataatlantica',
            name='compensacao_estagio_medi',
            field=models.FloatField(blank=True, verbose_name='Área de Compensação de Estágio Medio (ha)', null=True),
        ),
        migrations.AddField(
            model_name='asvmataatlantica',
            name='compensacao_vegetacao_prim',
            field=models.FloatField(blank=True, verbose_name='Área de Compensação de Vegetação Primária (ha)', null=True),
        ),
        migrations.AddField(
            model_name='asvmataatlantica',
            name='observacoes',
            field=models.TextField(blank=True, verbose_name='Obeservções', null=True),
        ),
        migrations.AddField(
            model_name='asvmataatlantica',
            name='tipo_compensacao',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
