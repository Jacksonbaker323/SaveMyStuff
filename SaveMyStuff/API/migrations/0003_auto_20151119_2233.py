# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20151119_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='owner',
            field=models.OneToOneField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
