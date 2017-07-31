# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20170728_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compensacaomataatlantica',
            old_name='area_compensacao',
            new_name='area_compensacao_total',
        ),
    ]
