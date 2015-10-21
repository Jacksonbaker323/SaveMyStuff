# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20150921_0039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='PropertyTypes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_owner',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
