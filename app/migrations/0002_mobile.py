# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-14 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=240)),
                ('sore', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('miao', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=20)),
            ],
        ),
    ]
