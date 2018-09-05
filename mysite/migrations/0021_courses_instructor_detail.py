# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_auto_20171214_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='instructor_detail',
            field=models.CharField(default=b'', max_length=500),
        ),
    ]
