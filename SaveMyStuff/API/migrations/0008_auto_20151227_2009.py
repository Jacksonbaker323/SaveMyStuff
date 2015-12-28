# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0007_auto_20151202_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Property_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('property_value', models.CharField(max_length=255)),
                ('item', models.ForeignKey(related_name='item', to='API.Item')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='display_property',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property_item',
            name='property',
            field=models.ForeignKey(related_name='property', to='API.Property'),
        ),
    ]
