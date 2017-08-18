# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20170818_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geompedidoanuenciamataatlantica',
            name='processo',
            field=models.ForeignKey(to_field='processo', blank=True, null=True, to='core.DadosAnuenciaMataAtlantica'),
        ),
    ]
