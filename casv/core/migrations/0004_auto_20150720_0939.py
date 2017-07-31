# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150720_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areasoltura',
            old_name='creation_date',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='areasoltura',
            old_name='user',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='asv',
            old_name='creation_date',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='asv',
            old_name='user',
            new_name='usuario',
        ),
    ]
