# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150805_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asv',
            options={'verbose_name': 'Autorização de Supressão de Vegetação', 'verbose_name_plural': 'Autorizações de Supressão de Vegetação'},
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='atividade',
            field=models.CharField(max_length=255, verbose_name='Atividade Econômica', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='bioma',
            field=models.CharField(max_length=255, verbose_name='Bioma', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='distancia',
            field=models.FloatField(verbose_name='Área da Propriedade (ha)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='endereco',
            field=models.CharField(max_length=400, verbose_name='Endereço', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='fitofisionomia',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='municipio',
            field=models.CharField(max_length=255, verbose_name='Município', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome da propriedade', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='proprietario',
            field=models.CharField(max_length=255, verbose_name='Nome do proprietário', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='tempo',
            field=models.FloatField(verbose_name='Tempo de viagem ao CETAS mais próximo', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='uf',
            field=models.CharField(max_length=2, verbose_name='Unidade da Federação', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='usuario',
            field=models.ForeignKey(related_name='area_soltura', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='vistoria',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='usuario',
            field=models.ForeignKey(related_name='asv', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='area_supressao_estagio_avancado',
            field=models.FloatField(verbose_name='Área de Supressão em\n        Estágio Avançado (ha)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='area_supressao_estagio_medio',
            field=models.FloatField(verbose_name='Área de Supressão em\n        Estágio Médio (ha)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='area_supressao_total',
            field=models.FloatField(verbose_name='Área Total de Supressão (ha)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='area_supressao_veg_primaria',
            field=models.FloatField(verbose_name='Área de Supressão de\n        Vegetação Primária (ha)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='cpfj',
            field=models.CharField(max_length=22, verbose_name='CPF ou CNPJ do Empreendedor', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='empreendedor',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='municipio',
            field=models.CharField(max_length=255, verbose_name='Município', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='processo',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='tipo_empreendimento',
            field=models.CharField(max_length=255, verbose_name='Tipo de Empreendimento', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='uf',
            field=models.CharField(max_length=2, verbose_name='Unidade da Federação', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='usuario',
            field=models.ForeignKey(related_name='asvma', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='area_compensacao',
            field=models.FloatField(verbose_name='Área de Compensação (ha)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='cpfj',
            field=models.CharField(max_length=22, verbose_name='CPF ou CNPJ do Empreendedor', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='empreendedor',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='municipio',
            field=models.CharField(max_length=255, verbose_name='Município', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='processo',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='tipo_empreendimento',
            field=models.CharField(max_length=255, verbose_name='Tipo de Empreendimento', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='uf',
            field=models.CharField(max_length=2, verbose_name='Unidade da Federação', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='usuario',
            field=models.ForeignKey(related_name='compensacao', to=settings.AUTH_USER_MODEL),
        ),
    ]
