# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0021_courses_instructor_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='number_of_lesson',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
