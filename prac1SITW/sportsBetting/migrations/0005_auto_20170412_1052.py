# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsBetting', '0004_event_team1'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='team2',
            field=models.ForeignKey(related_name='visitor', to='sportsBetting.Team', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='team1',
            field=models.ForeignKey(related_name='local', to='sportsBetting.Team', null=True),
        ),
    ]
