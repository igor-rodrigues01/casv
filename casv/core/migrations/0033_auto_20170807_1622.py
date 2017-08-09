# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20170807_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geomanuenciaconcedidamataatlantica',
            name='processo',
            field=models.OneToOneField(to='core.DadosAnuenciaMataAtlantica', to_field='processo'),
        ),
        migrations.AlterField(
            model_name='geompedidoanuenciamataatlantica',
            name='processo',
            field=models.OneToOneField(to='core.DadosAnuenciaMataAtlantica', to_field='processo'),
        ),
    ]
