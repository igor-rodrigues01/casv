# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_geomanuenciaconcedidamataatlantica_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geomanuenciaconcedidamataatlantica',
            name='processo',
            field=models.ForeignKey(null=True, to_field='processo', blank=True, to='core.DadosAnuenciaMataAtlantica'),
        ),
    ]
