# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20170727_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='a_est_avan',
            new_name='area_supressao_estagio_avancado',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='a_est_med',
            new_name='area_supressao_estagio_medio',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='area_total',
            new_name='area_supressao_total',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='a_veg_prim',
            new_name='area_supressao_veg_primaria',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='empreended',
            new_name='empreendedor',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='tipo_empre',
            new_name='tipo_empreendimento',
        ),
    ]
