# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsBetting', '0014_team_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='short_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]