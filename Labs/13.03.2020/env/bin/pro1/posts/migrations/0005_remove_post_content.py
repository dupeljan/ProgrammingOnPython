# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 11:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200313_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]