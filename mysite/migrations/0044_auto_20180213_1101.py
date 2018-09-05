# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0043_auto_20180213_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='course_video_1_duration',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='course_video_2_duration',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='course_video_3_duration',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='course_video_4_duration',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='course_video_5_duration',
        ),
    ]
