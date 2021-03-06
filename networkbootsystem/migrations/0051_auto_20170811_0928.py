# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkbootsystem', '0050_auto_20170811_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disksmartinfo',
            name='capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='实际容量G'),
        ),
        migrations.AlterField(
            model_name='disksmartinfo',
            name='size',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, verbose_name='硬盘大小G'),
        ),
    ]
