# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20151119_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('property_name', models.CharField(max_length=200)),
                ('property_type', models.CharField(max_length=1, choices=[('I', 'Integer'), ('S', 'String'), ('D', 'Date')])),
            ],
            options={
                'ordering': (),
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='categories'),
        ),
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.ForeignKey(to='API.Category', related_name='category'),
        ),
    ]
