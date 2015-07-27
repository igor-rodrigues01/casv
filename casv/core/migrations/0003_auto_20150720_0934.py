# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_areasoltura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asv',
            name='upload_date',
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 20, 9, 33, 58, 356132), verbose_name='Creation Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areasoltura',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asv',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 20, 9, 34, 15, 204088), verbose_name='Creation Date'),
            preserve_default=False,
        ),
    ]
