# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import yiyaweb.models


class Migration(migrations.Migration):

    dependencies = [
        ('yiyaweb', '0002_remove_application_other_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='other_file',
            field=models.FileField(blank=True, null=True, upload_to=yiyaweb.models.other_path),
        ),
    ]
