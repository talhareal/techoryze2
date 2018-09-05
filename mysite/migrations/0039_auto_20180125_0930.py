# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0038_auto_20180125_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='course_video_5_duration',
            new_name='course_video_5_durations',
        ),
    ]
