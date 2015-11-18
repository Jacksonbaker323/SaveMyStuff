# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': (),
            },
        ),
    ]
