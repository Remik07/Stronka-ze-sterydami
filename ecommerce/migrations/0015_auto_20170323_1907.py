# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_delete_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(default='{% static "ecommerce/steryd.png" %}', upload_to='{% static "ecommerce/" %}'),
        ),
    ]
