# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_auto_20170322_2036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]
