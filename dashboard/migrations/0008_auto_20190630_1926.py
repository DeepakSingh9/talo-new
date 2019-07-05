# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-30 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_profile_blocked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='blocked_by',
        ),
        migrations.AddField(
            model_name='profile',
            name='block',
            field=models.ManyToManyField(related_name='blocked_by', to='dashboard.Profile'),
        ),
    ]
