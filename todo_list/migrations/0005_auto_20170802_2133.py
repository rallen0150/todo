# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_auto_20170725_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
