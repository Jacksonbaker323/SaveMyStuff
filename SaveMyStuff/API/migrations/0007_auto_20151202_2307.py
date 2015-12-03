# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(max_length=1, choices=[('S', 'String'), ('I', 'Integer'), ('D', 'Date'), ('P', 'Image')]),
        ),
    ]
