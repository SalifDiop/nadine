# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nadine', '0025_assigned_alerts'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
    ]