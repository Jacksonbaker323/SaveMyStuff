# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='property',
        ),
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.OneToOneField(default=1, to='API.Category', related_name='category'),
            preserve_default=False,
        ),
    ]
