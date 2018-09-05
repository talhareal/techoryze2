# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0034_auto_20180119_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='About_video',
            field=models.FileField(default=b'', upload_to='video/', blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='About_video_WebmFormat',
            field=models.FileField(default=b'', upload_to='video/', blank=True),
        ),
    ]
