# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20170314_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
