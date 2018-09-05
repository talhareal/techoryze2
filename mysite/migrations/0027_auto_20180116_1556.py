# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0026_auto_20171226_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_video',
            field=models.FileField(default=b'', upload_to='http://ec2-54-84-36-230.compute-1.amazonaws.com/'),
        ),
    ]
