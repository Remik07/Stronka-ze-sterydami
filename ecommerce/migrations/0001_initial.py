# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.FloatField(max_length=200)),
                ('years', models.FloatField(max_length=200)),
                ('rate', models.FloatField(max_length=200)),
                ('amount', models.FloatField(max_length=200)),
            ],
        ),
    ]
