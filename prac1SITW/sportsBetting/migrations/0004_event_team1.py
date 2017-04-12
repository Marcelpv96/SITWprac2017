# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsBetting', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='team1',
            field=models.ForeignKey(to='sportsBetting.Team', null=True),
        ),
    ]
