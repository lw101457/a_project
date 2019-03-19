# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=256)),
                ('token', models.CharField(max_length=256)),
            ],
        ),
    ]
