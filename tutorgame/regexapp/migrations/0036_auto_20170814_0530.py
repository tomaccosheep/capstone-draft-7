# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexapp', '0035_auto_20170814_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_num',
            name='unique_id',
            field=models.CharField(default='fToO1AQzRpLpv3PkWpBN7En6tnaTOIXT', max_length=32, primary_key=True, serialize=False),
        ),
    ]