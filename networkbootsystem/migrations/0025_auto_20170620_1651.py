# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networkbootsystem', '0024_auto_20170620_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='auth_alter',
            new_name='auth_update',
        ),
    ]
