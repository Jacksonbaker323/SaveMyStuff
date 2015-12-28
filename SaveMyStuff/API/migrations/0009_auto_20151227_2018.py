# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_auto_20151227_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('property_value', models.CharField(max_length=255)),
                ('item', models.ForeignKey(to='API.Item', related_name='item')),
                ('property', models.ForeignKey(to='API.Property', related_name='property')),
            ],
        ),
        migrations.RemoveField(
            model_name='property_item',
            name='item',
        ),
        migrations.RemoveField(
            model_name='property_item',
            name='property',
        ),
        migrations.DeleteModel(
            name='Property_Item',
        ),
    ]
