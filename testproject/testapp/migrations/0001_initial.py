# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-05 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jungle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('area', models.PositiveIntegerField()),
                ('apex_predator', models.CharField(max_length=200)),
            ],
        ),
    ]