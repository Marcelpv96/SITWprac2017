# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsBetting', '0021_competition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='crest',
            field=models.ImageField(null=True, upload_to=b'crests/'),
        ),
    ]
