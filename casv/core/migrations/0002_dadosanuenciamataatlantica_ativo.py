# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosanuenciamataatlantica',
            name='ativo',
            field=models.BooleanField(verbose_name='Dados Ativos', default=True),
        ),
    ]
