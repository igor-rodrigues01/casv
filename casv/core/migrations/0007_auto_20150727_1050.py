# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150723_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asv',
            name='area_ha',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='codigo',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='data_autex',
            field=models.DateField(null=True, blank=True, verbose_name='Data de Autorização de Extração'),
        ),
        migrations.AlterField(
            model_name='asv',
            name='lenha_st',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='mourao_m',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='tora_m',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='torete_m',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='valido_ate',
            field=models.DateField(null=True, blank=True, verbose_name='Data de Validade da Autorização'),
        ),
    ]
