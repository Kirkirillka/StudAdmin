# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ticket',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studadmin.Speciality'),
        ),
    ]
