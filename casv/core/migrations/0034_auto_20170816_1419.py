# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0033_auto_20170807_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='geomanuenciaconcedidamataatlantica',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='geom_anuencia_concedida', null=True),
        ),
        migrations.AddField(
            model_name='geompedidoanuenciamataatlantica',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='geom_pedido_anuencia', null=True),
        ),
        migrations.AlterField(
            model_name='geomanuenciaconcedidamataatlantica',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674, verbose_name='Geometria'),
        ),
        migrations.AlterField(
            model_name='geomanuenciaconcedidamataatlantica',
            name='processo',
            field=models.ForeignKey(to='core.DadosAnuenciaMataAtlantica', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='geompedidoanuenciamataatlantica',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674, verbose_name='Geometria'),
        ),
        migrations.AlterField(
            model_name='geompedidoanuenciamataatlantica',
            name='processo',
            field=models.OneToOneField(to_field='processo', to='core.DadosAnuenciaMataAtlantica', blank=True, null=True),
        ),
    ]
