# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0048_auto_20180213_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechoryzeAnalytics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AppID', models.CharField(default=b'', max_length=50)),
                ('Username', models.CharField(default=b'', max_length=50)),
                ('AssetID', models.CharField(default=b'', max_length=50)),
                ('PageID', models.CharField(default=b'', max_length=50)),
                ('Page_Title', models.CharField(default=b'', max_length=30)),
                ('Asset_Title', models.CharField(default=b'', max_length=30)),
                ('Asset_Type', models.CharField(default=b'', max_length=30)),
                ('DateTime', models.CharField(default=b'', max_length=50)),
            ],
            options={
                'verbose_name': 'Techoryze Analytics',
                'verbose_name_plural': 'Techoryze Analytics',
            },
        ),
        migrations.DeleteModel(
            name='TechoryzeAnalytic',
        ),
    ]
