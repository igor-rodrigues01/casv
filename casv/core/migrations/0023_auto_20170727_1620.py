# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20170727_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='area_supressao_estagio_avancado',
            new_name='a_est_avan',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='area_supressao_estagio_medio',
            new_name='a_est_medi',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='area_supressao_veg_primaria',
            new_name='a_veg_prim',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='area_supressao_total',
            new_name='area_total',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='empreendedor',
            new_name='empreended',
        ),
        migrations.RenameField(
            model_name='asvmataatlantica',
            old_name='tipo_empreendimento',
            new_name='tipo_empre',
        ),
    ]
