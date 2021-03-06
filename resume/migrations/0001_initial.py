# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-16 08:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masters_degree_name', models.CharField(blank=True, default='', max_length=150)),
                ('masters_college_name', models.CharField(blank=True, max_length=150)),
                ('masters_education_from', models.DateField(default=datetime.date.today)),
                ('masters_education_till', models.DateField(default=datetime.date.today)),
                ('bachelors_degree', models.CharField(blank=True, max_length=150)),
                ('bachelors_college_name', models.CharField(blank=True, max_length=150)),
                ('bachelors_education_from', models.DateField(default=datetime.date.today)),
                ('bachelors_education_till', models.DateField(default=datetime.date.today)),
                ('High_School_degree', models.CharField(blank=True, max_length=150)),
                ('High_School_name', models.CharField(blank=True, max_length=150)),
                ('High_School_from', models.DateField(default=datetime.date.today)),
                ('High_School_till', models.DateField(default=datetime.date.today)),
                ('Junior_degree', models.CharField(blank=True, max_length=150)),
                ('Junior_School_name', models.CharField(blank=True, max_length=150)),
                ('Junior_School_from', models.DateField(default=datetime.date.today)),
                ('Junior_School_till', models.DateField(default=datetime.date.today)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Profile')),
            ],
        ),
    ]
