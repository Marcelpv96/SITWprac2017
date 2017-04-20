# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsBetting', '0007_auto_20170412_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='quota',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
