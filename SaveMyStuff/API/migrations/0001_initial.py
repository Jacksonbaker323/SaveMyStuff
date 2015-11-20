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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('category_name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': (),
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('property_name', models.CharField(max_length=200)),
                ('property_type', models.CharField(max_length=1, choices=[('I', 'Integer'), ('S', 'String'), ('D', 'Date')])),
            ],
            options={
                'ordering': (),
            },
        ),
        migrations.AddField(
            model_name='category',
            name='property',
            field=models.ForeignKey(related_name='properties', to='API.Property'),
        ),
    ]
