# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0044_auto_20180213_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='TechoryzeAnalytic',
            name='User_Email',
        ),
        migrations.AddField(
            model_name='TechoryzeAnalytic',
            name='Username',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
