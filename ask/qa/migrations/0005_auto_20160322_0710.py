# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 07:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0004_auto_20160315_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-id']},
        ),
    ]