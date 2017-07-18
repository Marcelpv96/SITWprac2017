# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 09:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sportsBetting', '0025_auto_20170525_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')], default=3, verbose_name=b'Rating\t(stars)')),
                ('comment', models.TextField(blank=True, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsBetting.Team')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='restaurantreview',
            unique_together=set([('team', 'user')]),
        ),
    ]