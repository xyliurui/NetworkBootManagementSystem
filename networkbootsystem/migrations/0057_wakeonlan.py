# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-26 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkbootsystem', '0056_auto_20170830_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='WakeOnLan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='MAC地址')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='最近执行')),
            ],
            options={
                'verbose_name': '网启开机',
                'verbose_name_plural': '网启开机日志',
            },
        ),
    ]