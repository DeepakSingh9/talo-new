# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-30 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20190628_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blocked_by',
            field=models.ManyToManyField(related_name='blocked', to='dashboard.Profile'),
        ),
    ]