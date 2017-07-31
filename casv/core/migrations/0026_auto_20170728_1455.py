# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20170727_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoanuenciamataatlantica',
            name='urbano_metropolitano',
            field=models.CharField(max_length=5, verbose_name='Local Urbarno'),
        ),
    ]
