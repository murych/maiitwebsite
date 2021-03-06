# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-22 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_auto_20160316_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='webpage',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='description',
            field=models.CharField(blank=True, default='Лектор', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_type',
            field=models.CharField(choices=[('org', 'Organizer'), ('lec', 'Lecturer'), ('par', 'Partner')], default='lec', max_length=3),
        ),
    ]
