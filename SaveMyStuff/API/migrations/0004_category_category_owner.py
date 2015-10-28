# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0003_auto_20151020_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_owner',
            field=models.ForeignKey(related_name='owner', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
