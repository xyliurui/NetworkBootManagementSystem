# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkbootsystem', '0064_questionbank_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='boot_clonezilla_id',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5, verbose_name='Clonezilla_ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='boot_iso_id',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5, verbose_name='Iso_ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='boot_select_id',
            field=models.CharField(blank=True, max_length=10, verbose_name='启动方式名称'),
        ),
    ]