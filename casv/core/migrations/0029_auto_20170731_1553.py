# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20170728_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuenciaconcedidamataatlantica',
            old_name='cpfj',
            new_name='cpf_cnpj',
        ),
        migrations.AlterField(
            model_name='anuenciaconcedidamataatlantica',
            name='urbano_metropolitano',
            field=models.CharField(max_length=5, verbose_name='Local Urbarno'),
        ),
        migrations.AlterField(
            model_name='anuenciaconcedidamataatlantica',
            name='usuario',
            field=models.ForeignKey(related_name='anuconcedmat', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pedidoanuenciamataatlantica',
            name='usuario',
            field=models.ForeignKey(related_name='pedanuencia', to=settings.AUTH_USER_MODEL),
        ),
    ]
