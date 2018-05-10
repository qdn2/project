# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-09 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20180508_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='z_restaurant',
            name='text',
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='food_type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='r_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='r_city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='r_cost',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='r_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='r_image',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='r_menu',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='r_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='z_restaurant',
            name='r_rating',
            field=models.CharField(max_length=200, null=True),
        ),
    ]