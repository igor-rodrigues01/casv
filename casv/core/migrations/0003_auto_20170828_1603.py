# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_dadosanuenciamataatlantica_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='geomanuenciaconcedidamataatlantica',
            name='area_ha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='geompedidoanuenciamataatlantica',
            name='area_ha',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
