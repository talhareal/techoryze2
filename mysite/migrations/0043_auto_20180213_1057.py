# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0042_auto_20180125_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechoryzeAnalytic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AppID', models.CharField(default=b'', max_length=50)),
                ('User_Email', models.CharField(default=b'', max_length=50)),
                ('AssetID', models.CharField(default=b'', max_length=50)),
                ('PageID', models.CharField(default=b'', max_length=50)),
                ('Page_Title', models.CharField(default=b'', max_length=30)),
                ('Asset_Title', models.CharField(default=b'', max_length=30)),
                ('Asset_Type', models.CharField(default=b'', max_length=30)),
                ('DateTime', models.CharField(default=b'', max_length=50)),
            ],
            options={
                'verbose_name': 'TechoryzeAnalytic',
                'verbose_name_plural': 'TechoryzeAnalytic',
            },
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_video_5_duration',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
