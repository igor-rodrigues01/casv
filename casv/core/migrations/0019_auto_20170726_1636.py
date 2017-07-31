# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20170725_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='c_est_avan',
            field=models.FloatField(verbose_name='Estágio Avançado de Regeneração', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='c_est_inic',
            field=models.FloatField(verbose_name='Estagio Inicial de Regeneração', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='c_est_medi',
            field=models.FloatField(verbose_name='Estágio Médio de Regeneração', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='c_veg_prim',
            field=models.FloatField(verbose_name='Vegetação Primária', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='obs',
            field=models.TextField(verbose_name='Obsercações', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compensacaomataatlantica',
            name='tipo_compensacao',
            field=models.CharField(verbose_name='Tipo De Compensação', blank=True, max_length=12, null=True),
        ),
    ]
