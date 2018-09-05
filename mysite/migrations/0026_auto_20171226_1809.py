# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0025_auto_20171221_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestopic',
            name='background_color',
            field=models.CharField(default=b'colorBlue mt-4', max_length=40, choices=[(b'colorBlue mt-4', b'BLUE'), (b'colorGreen mt-4', b'GREEN'), (b'colorparpup mt-4', b'PARPUL'), (b'colorOrange mt-4', b'ORANGE'), (b'colorpink mt-4', b'PINK'), (b'colorbrown mt-4', b'BROWN')]),
        ),
    ]
