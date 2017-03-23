# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20170322_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paymentmethodid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='productid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='billingaddressid',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productid',
        ),
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.CharField(default=' test ', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Name',
            field=models.CharField(default=' test', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.CharField(default='12', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='ProductID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Paymentmethod',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]