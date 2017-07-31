# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areasoltura',
            name='distancia',
            field=models.FloatField(null=True, verbose_name='Distância até o CETAS mais próximo', blank=True),
        ),
        migrations.AlterField(
            model_name='asv',
            name='area_ha',
            field=models.FloatField(null=True, verbose_name='Área da Propriedade (ha)', blank=True),
        ),
    ]
