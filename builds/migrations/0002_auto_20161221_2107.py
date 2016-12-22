# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 03:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
