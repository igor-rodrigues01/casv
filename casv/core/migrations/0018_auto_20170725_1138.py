# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20160106_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areasoltura',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674),
        ),
        migrations.AlterField(
            model_name='asv',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674),
        ),
        migrations.AlterField(
            model_name='asvmataatlantica',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674),
        ),
        migrations.AlterField(
            model_name='autoinfracaooema',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4674),
        ),
        migrations.AlterField(
            model_name='compensacaomataatlantica',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674),
        ),
        migrations.AlterField(
            model_name='embargooema',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4674),
        ),
    ]
