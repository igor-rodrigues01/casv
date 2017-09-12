# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150729_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areasoltura',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF', null=True, blank=True),
        )
    ]
