# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_myuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='company',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
