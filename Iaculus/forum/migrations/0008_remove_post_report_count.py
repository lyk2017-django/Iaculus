# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 12:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20170802_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='report_count',
        ),
    ]
