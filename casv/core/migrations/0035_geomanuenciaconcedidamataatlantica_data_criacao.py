# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20170816_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='geomanuenciaconcedidamataatlantica',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação', null=True),
        ),
    ]
