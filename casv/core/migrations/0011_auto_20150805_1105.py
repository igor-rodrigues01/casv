# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150804_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areasoltura',
            name='viveiro',
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='viveiros',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Número de viveiros', blank=True),
        ),
    ]
