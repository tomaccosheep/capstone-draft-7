# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexapp', '0005_auto_20170813_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_num',
            name='unique_id',
            field=models.CharField(default='HLt6AoIOIxfGeFilVNJOnxOB8teOYfSO', max_length=32, primary_key=True, serialize=False),
        ),
    ]
