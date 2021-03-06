# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studadmin', '0013_student_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='staff',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='violation',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='violation',
            name='student',
        ),
        migrations.AddField(
            model_name='violation',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='studadmin.Student'),
        ),
    ]
