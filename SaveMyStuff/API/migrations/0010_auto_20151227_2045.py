# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_auto_20151227_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ()},
        ),
        migrations.RemoveField(
            model_name='property',
            name='display_property',
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='DELETEME', max_length=255),
            preserve_default=False,
        ),
    ]
