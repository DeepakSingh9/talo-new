# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-21 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20190313_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followed_by',
            field=models.ManyToManyField(related_name='follows', to='dashboard.Profile'),
        ),
    ]