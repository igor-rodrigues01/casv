# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150811_1144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areasoltura',
            options={'verbose_name': 'Área de Soltura de Animais Silvestres', 'verbose_name_plural': 'Áreas de Soltura de Animais Silvestres'},
        ),
        migrations.AlterModelOptions(
            name='asvmataatlantica',
            options={'verbose_name': 'Autorização de Supressão de Vegetação - Mata Atlântica', 'verbose_name_plural': 'Autorizações de Supressão de Vegetação -\n            Mata Atlântica'},
        ),
        migrations.AlterModelOptions(
            name='compensacaomataatlantica',
            options={'verbose_name': 'Área de Compensação - Mata Atlântica', 'verbose_name_plural': 'Áreas de Compensação - Mata Atlântica'},
        ),
        migrations.AlterField(
            model_name='areasoltura',
            name='email',
            field=models.EmailField(null=True, max_length=254, blank=True),
        ),
    ]
