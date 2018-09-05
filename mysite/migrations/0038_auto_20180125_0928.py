# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0037_auto_20180125_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_video_5_duration',
            field=models.DurationField(),
        ),
    ]
