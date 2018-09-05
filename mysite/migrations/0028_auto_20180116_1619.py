# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0027_auto_20180116_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_video',
            field=models.FileField(default=b'', upload_to='video/'),
        ),
    ]
