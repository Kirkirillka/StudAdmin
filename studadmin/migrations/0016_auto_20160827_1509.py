# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studadmin', '0015_violation_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='violation',
            name='room',
        ),
        migrations.AddField(
            model_name='student',
            name='room',
            field=models.IntegerField(default=0),
        ),
    ]
