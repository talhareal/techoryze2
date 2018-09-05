# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_courses_number_of_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_video',
            field=models.FileField(default=b'', upload_to='video/'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='number_of_lesson',
            field=models.IntegerField(default=0),
        ),
    ]
