# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]