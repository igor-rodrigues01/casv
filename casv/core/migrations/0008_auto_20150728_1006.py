# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150727_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areasoltura',
            name='agua',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='area',
            field=models.FloatField(blank=True, verbose_name='Área da Propriedade (ha)', null=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='arl_app',
            field=models.FloatField(blank=True, verbose_name='Área de reserva legal e proteção permanente', null=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='carta',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='conectividade',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='conservacao',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='cpf',
            field=models.BigIntegerField(blank=True, verbose_name='CPF', null=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='documento',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='mapa',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='processo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='reabilitador',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='telefone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='uc',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='viveiro',
            field=models.IntegerField(blank=True, verbose_name='Número de viveiros', null=True),
        ),
    ]
