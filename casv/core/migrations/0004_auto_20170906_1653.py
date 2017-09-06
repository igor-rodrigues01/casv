# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170828_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadosanuenciamataatlantica',
            name='area_empreendimento_total',
        ),
        migrations.AlterField(
            model_name='geomanuenciaconcedidamataatlantica',
            name='area_ha',
            field=models.FloatField(verbose_name='Área (ha)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='geompedidoanuenciamataatlantica',
            name='area_ha',
            field=models.FloatField(verbose_name='Área (ha)', blank=True, null=True),
        ),
    ]
