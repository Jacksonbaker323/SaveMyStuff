# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20151119_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
