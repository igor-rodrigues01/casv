# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20170731_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compensacaomataatlantica',
            options={'verbose_name': 'Área de Compensação - Mata Atlântica', 'verbose_name_plural': 'Áreas de Compensações - Mata Atlântica'},
        ),
        migrations.AlterField(
            model_name='anuenciaconcedidamataatlantica',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='anuenciaconcedida'),
        ),
    ]
