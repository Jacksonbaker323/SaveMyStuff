# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20151119_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('property_name', models.CharField(max_length=200)),
                ('property_type', models.CharField(max_length=1, choices=[('S', 'String'), ('I', 'Int'), ('D', 'Date'), ('C', 'Currency')])),
                ('category', models.ForeignKey(related_name='category', to='API.Category')),
            ],
            options={
                'ordering': (),
            },
        ),
    ]
