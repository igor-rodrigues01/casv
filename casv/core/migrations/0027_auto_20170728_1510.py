# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20170728_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compensacaomataatlantica',
            old_name='area_conpensacao_estagio_avancado',
            new_name='area_compensacao_estagio_avancado',
        ),
        migrations.RenameField(
            model_name='compensacaomataatlantica',
            old_name='area_conpensacao_estagio_inicial',
            new_name='area_compensacao_estagio_inicial',
        ),
        migrations.RenameField(
            model_name='compensacaomataatlantica',
            old_name='area_conpensacao_estagio_medio',
            new_name='area_compensacao_estagio_medio',
        ),
        migrations.RenameField(
            model_name='compensacaomataatlantica',
            old_name='area_conpensacao_veg_primaria',
            new_name='area_compensacao_veg_primaria',
        ),
    ]
