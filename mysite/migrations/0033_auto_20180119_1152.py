# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0032_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='About_video_1',
            new_name='About_video',
        ),
    ]
