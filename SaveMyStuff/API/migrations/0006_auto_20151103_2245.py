# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20151103_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_owner',
        ),
    ]
