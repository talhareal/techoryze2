# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0047_auto_20180213_1238'),
    ]

    operations = [
        migrations.RenameField('TechoryzeAnalytic', 'User_Email', 'Username'),
    ]


