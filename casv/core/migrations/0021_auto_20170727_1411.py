# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20170726_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuenciaconcedidamataatlantica',
            name='area_supressao_estagio_avancado',
        ),
        migrations.RemoveField(
            model_name='anuenciaconcedidamataatlantica',
            name='area_supressao_estagio_medio',
        ),
        migrations.RemoveField(
            model_name='anuenciaconcedidamataatlantica',
            name='area_supressao_total',
        ),
        migrations.RemoveField(
            model_name='anuenciaconcedidamataatlantica',
            name='area_supressao_veg_primaria',
        ),
        migrations.RemoveField(
            model_name='anuenciaconcedidamataatlantica',
            name='observacoes',
        ),
        migrations.RemoveField(
            model_name='asvmataatlantica',
            name='compensacao_estagio_avan',
        ),
        migrations.RemoveField(
            model_name='asvmataatlantica',
            name='compensacao_estagio_inic',
        ),
        migrations.RemoveField(
            model_name='asvmataatlantica',
            name='compensacao_estagio_medi',
        ),
        migrations.RemoveField(
            model_name='asvmataatlantica',
            name='compensacao_vegetacao_prim',
        ),
        migrations.RemoveField(
            model_name='asvmataatlantica',
            name='observacoes',
        ),
        migrations.RemoveField(
            model_name='asvmataatlantica',
            name='tipo_compensacao',
        ),
        migrations.RemoveField(
            model_name='pedidoanuenciamataatlantica',
            name='area_supressao_estagio_avancado',
        ),
        migrations.RemoveField(
            model_name='pedidoanuenciamataatlantica',
            name='area_supressao_estagio_medio',
        ),
        migrations.RemoveField(
            model_name='pedidoanuenciamataatlantica',
            name='area_supressao_total',
        ),
        migrations.RemoveField(
            model_name='pedidoanuenciamataatlantica',
            name='area_supressao_veg_primaria',
        ),
        migrations.RemoveField(
            model_name='pedidoanuenciamataatlantica',
            name='observacoes',
        ),
        migrations.AddField(
            model_name='anuenciaconcedidamataatlantica',
            name='area_empreendimento_estagio_avancado',
            field=models.FloatField(null=True, verbose_name='Área de Empreendimento em Estágio Avançado (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='anuenciaconcedidamataatlantica',
            name='area_empreendimento_estagio_medio',
            field=models.FloatField(null=True, verbose_name='Área de Empreendimento em Estágio Médio (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='anuenciaconcedidamataatlantica',
            name='area_empreendimento_total',
            field=models.FloatField(null=True, verbose_name='Área Total de Empreendimento (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='anuenciaconcedidamataatlantica',
            name='area_empreendimento_veg_primaria',
            field=models.FloatField(null=True, verbose_name='Área Empreendida em Vegetação Primária (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='anuenciaconcedidamataatlantica',
            name='observacao',
            field=models.TextField(null=True, verbose_name='Observação', blank=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='area_conpensacao_estagio_avancado',
            field=models.FloatField(null=True, verbose_name='Área de Compensação em Estágio Avançado (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='area_conpensacao_estagio_inicial',
            field=models.FloatField(null=True, verbose_name='Área de Compensação em Estágio Inicial (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='area_conpensacao_estagio_medio',
            field=models.FloatField(null=True, verbose_name='Área de Compensação em Estágio Médio (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='area_conpensacao_veg_primaria',
            field=models.FloatField(null=True, verbose_name='Área de Compensação de Vegetação Primária (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='observacao',
            field=models.TextField(null=True, verbose_name='Observação', blank=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='tipo_compensacao',
            field=models.CharField(null=True, blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='pedidoanuenciamataatlantica',
            name='area_empreendimento_estagio_avancado',
            field=models.FloatField(null=True, verbose_name='Área de Empreendimento em Estágio Avançado (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='pedidoanuenciamataatlantica',
            name='area_empreendimento_estagio_medio',
            field=models.FloatField(null=True, verbose_name='Área de Empreendimento em Estágio Médio (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='pedidoanuenciamataatlantica',
            name='area_empreendimento_total',
            field=models.FloatField(null=True, verbose_name='Área Total de Empreendimento (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='pedidoanuenciamataatlantica',
            name='area_empreendimento_veg_primaria',
            field=models.FloatField(null=True, verbose_name='Área Empreendida em Vegetação Primária (ha)', blank=True),
        ),
        migrations.AddField(
            model_name='pedidoanuenciamataatlantica',
            name='observacao',
            field=models.TextField(null=True, verbose_name='Observação', blank=True),
        ),
        migrations.AlterField(
            model_name='anuenciaconcedidamataatlantica',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='anuConcedMat'),
        ),
        migrations.AlterField(
            model_name='pedidoanuenciamataatlantica',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='pedAnuMat'),
        ),
    ]
