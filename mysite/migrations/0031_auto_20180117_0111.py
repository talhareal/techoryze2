# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0030_auto_20180116_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_video',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
