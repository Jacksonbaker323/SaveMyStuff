# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_category_category_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ()},
        ),
        migrations.AddField(
            model_name='category',
            name='category_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 4, 6, 25, 37, 440238, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
