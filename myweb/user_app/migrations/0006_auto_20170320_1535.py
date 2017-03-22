# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_auto_20170318_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('borrow_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='file',
        ),
        migrations.AddField(
            model_name='object',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.User'),
        ),
        migrations.AlterField(
            model_name='object',
            name='objectnum',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='order',
            name='object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.Object'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.User'),
        ),
    ]