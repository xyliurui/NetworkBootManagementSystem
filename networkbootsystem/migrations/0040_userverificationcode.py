# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-03 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkbootsystem', '0039_user_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVerificationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('verify', models.CharField(blank=True, max_length=10, verbose_name='验证码')),
                ('outbox', models.CharField(blank=True, max_length=10, verbose_name='发件箱')),
                ('inbox', models.CharField(blank=True, max_length=10, verbose_name='收件箱')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]
