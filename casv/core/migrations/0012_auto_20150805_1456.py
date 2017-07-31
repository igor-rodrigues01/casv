# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150805_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areasoltura',
            name='telefone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
