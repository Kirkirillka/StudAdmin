# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studadmin', '0007_auto_20160814_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='student',
        ),
        migrations.AddField(
            model_name='promotion',
            name='student',
            field=models.ManyToManyField(default=None, to='studadmin.Student'),
        ),
    ]
