# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0039_auto_20180125_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='course_video_5_durations',
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_5_duration',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
