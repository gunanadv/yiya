# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiyaweb', '0003_application_other_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='birth_country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='application',
            name='birth_province',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
