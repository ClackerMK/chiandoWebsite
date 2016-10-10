# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChianDoWebsite', '0010_auto_20161009_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='gps_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='gps_lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
