# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 11:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170724_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 24, 11, 28, 51, 344692, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]