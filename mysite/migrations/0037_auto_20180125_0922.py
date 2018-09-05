# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0036_auto_20180123_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_video_1_duration',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_2_duration',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_3_duration',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_4_duration',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_5_duration',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
