# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-24 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0013_auto_20160724_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]