# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_auto_20170323_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.TextField(blank=True, db_column='Image', null=True),
        ),
    ]
