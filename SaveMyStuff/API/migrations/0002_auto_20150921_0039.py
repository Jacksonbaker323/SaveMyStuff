# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('property_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTypes',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('property_type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='owner',
            new_name='category_owner',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_name',
        ),
    ]
