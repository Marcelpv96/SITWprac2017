# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsBetting', '0015_auto_20170510_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='api_id',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
