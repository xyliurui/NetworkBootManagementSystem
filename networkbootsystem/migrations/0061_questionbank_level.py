# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-29 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkbootsystem', '0060_auto_20170929_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionbank',
            name='level',
            field=models.CharField(default='普通', max_length=10, verbose_name='难易程度'),
            preserve_default=False,
        ),
    ]
