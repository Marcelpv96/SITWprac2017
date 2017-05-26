# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsBetting', '0006_bet'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='quota',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
