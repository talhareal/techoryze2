# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0033_auto_20180119_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='About_video',
        ),
        migrations.AddField(
            model_name='about',
            name='About_video_OggFormat',
            field=models.FileField(default=b'', upload_to='video/', blank=True),
        ),
    ]
