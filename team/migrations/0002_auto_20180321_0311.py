# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planpost',
            options={'ordering': ('modify_date',), 'verbose_name': 'planpost', 'verbose_name_plural': 'planposts'},
        ),
    ]
