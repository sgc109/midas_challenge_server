# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 02:03
from __future__ import unicode_literals

import account_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0004_auto_20180519_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=account_app.models.get_image_path),
        ),
    ]