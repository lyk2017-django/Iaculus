# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20170725_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]