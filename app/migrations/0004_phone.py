# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-14 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190114_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
                ('Price', models.CharField(max_length=20)),
            ],
        ),
    ]
