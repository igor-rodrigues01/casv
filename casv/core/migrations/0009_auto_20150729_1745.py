# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150728_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asv',
            name='cpfj_dete',
            field=models.CharField(null=True, blank=True, verbose_name='CPF ou CNPJ do Detentor', max_length=22),
        ),
        migrations.AlterField(
            model_name='asv',
            name='cpfj_prop',
            field=models.CharField(null=True, blank=True, verbose_name='CPF ou CNPJ do Proprietário', max_length=22),
        ),
        migrations.AlterField(
            model_name='asv',
            name='cpfj_rt',
            field=models.CharField(null=True, blank=True, max_length=22),
        ),
        migrations.AlterField(
            model_name='asv',
            name='detentor',
            field=models.CharField(null=True, blank=True, verbose_name='Nome do Detentor', max_length=60),
        ),
        migrations.AlterField(
            model_name='asv',
            name='fito',
            field=models.CharField(null=True, blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='asv',
            name='municipio',
            field=models.CharField(null=True, blank=True, verbose_name='Município', max_length=40),
        ),
        migrations.AlterField(
            model_name='asv',
            name='n_autex',
            field=models.CharField(null=True, blank=True, verbose_name='Número de Autorização de Extração', max_length=30),
        ),
        migrations.AlterField(
            model_name='asv',
            name='nom_prop',
            field=models.CharField(null=True, blank=True, verbose_name='Nome do Proprietário', max_length=60),
        ),
        migrations.AlterField(
            model_name='asv',
            name='rt',
            field=models.CharField(null=True, blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='asv',
            name='uf',
            field=models.CharField(null=True, blank=True, verbose_name='UF', max_length=2),
        ),
    ]
