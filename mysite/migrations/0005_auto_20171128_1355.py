# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20171128_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesmodel1',
            name='course_author_image',
            field=models.ImageField(null=True, upload_to=b'http://54.197.43.10/static/images', blank=True),
        ),
        migrations.AlterField(
            model_name='coursesmodel1',
            name='course_thumbanilImage',
            field=models.ImageField(null=True, upload_to=b'http://54.197.43.10/static/images', blank=True),
        ),
    ]
