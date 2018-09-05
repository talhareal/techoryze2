# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_auto_20171213_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Add Courses', 'verbose_name_plural': 'Add Courses'},
        ),
        migrations.AlterModelOptions(
            name='coursestopic',
            options={'verbose_name': 'Course Topics', 'verbose_name_plural': 'Course Topics'},
        ),
        migrations.AddField(
            model_name='courses',
            name='course_outline',
            field=models.CharField(default=b'', max_length=500),
        ),
    ]
