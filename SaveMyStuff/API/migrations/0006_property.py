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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('property_name', models.CharField(max_length=200)),
                ('property_type', models.CharField(max_length=1, choices=[('St', 'String'), ('I', 'Integer'), ('D', 'Date'), ('P', 'Image')])),
                ('category', models.ForeignKey(related_name='properties', to='API.Category')),
            ],
            options={
                'ordering': (),
            },
        ),
    ]
