# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0035_auto_20180119_1258'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_video',
            field=models.FileField(default=b'', upload_to='video/', blank=True),
        ),
    ]
