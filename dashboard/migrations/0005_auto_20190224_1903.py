# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 13:33
from __future__ import unicode_literals

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190224_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilecontact',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]