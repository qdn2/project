# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-09 00:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20180508_1904'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Z_Restaurants',
            new_name='Z_Restaurant',
        ),
    ]
