# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='types',
            name='pid',
            field=models.IntegerField(),
        ),
    ]
