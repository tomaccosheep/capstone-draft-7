# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexapp', '0011_auto_20170813_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_num',
            name='unique_id',
            field=models.CharField(default='7w3mJYN4OoaNhLGLzX2LITDUSNNEsOAQ', max_length=32, primary_key=True, serialize=False),
        ),
    ]
