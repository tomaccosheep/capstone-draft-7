# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card_manager',
            name='id',
        ),
        migrations.AlterField(
            model_name='card_manager',
            name='unique_id',
            field=models.CharField(default='TBNy5kCQf32oouNS1800HBgV5kPRSbTM', max_length=32, primary_key=True, serialize=False),
        ),
    ]
