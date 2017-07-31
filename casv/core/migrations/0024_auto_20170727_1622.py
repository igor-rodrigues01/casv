# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20170727_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='a_est_medi',
            new_name='a_est_med',
        ),
    ]
