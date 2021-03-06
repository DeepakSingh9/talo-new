# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-18 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190616_2009'),
        ('resume', '0005_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.DateField()),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True)),
                ('cert_image', models.FileField(blank=True, upload_to='cert_images/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Profile')),
            ],
        ),
    ]
