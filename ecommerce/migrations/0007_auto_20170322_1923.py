# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_auto_20170322_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='basket',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='basket',
            name='price',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='basket',
            name='productid',
            field=models.IntegerField(),
        ),
    ]
