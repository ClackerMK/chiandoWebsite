# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChianDoWebsite', '0002_auto_20160914_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
