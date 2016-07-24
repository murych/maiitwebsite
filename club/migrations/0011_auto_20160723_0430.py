# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-23 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(default='https://github.com/', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_type',
            field=models.CharField(choices=[('org', 'Organizer'), ('lec', 'Lecturer')], default='lec', max_length=3),
        ),
        migrations.AlterField(
            model_name='partner',
            name='url',
            field=models.URLField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]