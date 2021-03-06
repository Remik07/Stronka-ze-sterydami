# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20170322_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressid', models.IntegerField(db_column='AddressId', primary_key=True, serialize=False)),
                ('addressline1', models.CharField(db_column='AddressLine1', max_length=255)),
                ('addressline2', models.CharField(db_column='AddressLine2', max_length=255)),
                ('postcode', models.CharField(db_column='PostCode', max_length=255)),
                ('city', models.CharField(db_column='City', max_length=255)),
                ('country', models.CharField(db_column='Country', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderid', models.IntegerField(db_column='OrderId', primary_key=True, serialize=False)),
                ('confirmed', models.NullBooleanField(db_column='Confirmed')),
            ],
        ),
        migrations.CreateModel(
            name='Paymentmethod',
            fields=[
                ('paymentmethodid', models.IntegerField(db_column='PaymentMethodId', primary_key=True, serialize=False)),
                ('cardnumber', models.CharField(db_column='CardNumber', max_length=255)),
                ('expdate', models.CharField(db_column='ExpDate', max_length=255)),
                ('cardholdername', models.CharField(db_column='CardHolderName', max_length=255)),
                ('billingaddressid', models.ForeignKey(db_column='BillingAddressId', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Address')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.IntegerField(db_column='UserId', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='Username', max_length=255)),
                ('password', models.CharField(db_column='Password', max_length=255)),
                ('firstname', models.CharField(db_column='FirstName', max_length=255)),
                ('lastname', models.CharField(db_column='LastName', max_length=255)),
                ('email', models.CharField(db_column='Email', max_length=255)),
                ('phonenumber', models.CharField(db_column='PhoneNumber', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='basket',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ProductID',
        ),
        migrations.AddField(
            model_name='basket',
            name='description',
            field=models.TextField(blank=True, db_column='Description', null=True),
        ),
        migrations.AddField(
            model_name='basket',
            name='name',
            field=models.CharField(blank=True, db_column='Name', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='basket',
            name='price',
            field=models.TextField(blank=True, db_column='Price', null=True),
        ),
        migrations.AddField(
            model_name='basket',
            name='productid',
            field=models.IntegerField(db_column='ProductId', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, db_column='Description', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, db_column='Name', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.TextField(blank=True, db_column='Price', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='productid',
            field=models.IntegerField(db_column='ProductId', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basket',
            name='StuffID_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='userid',
            field=models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentmethodid',
            field=models.ForeignKey(blank=True, db_column='PaymentMethodId', null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Paymentmethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='productid',
            field=models.ManyToManyField(db_column='ProductId', to='ecommerce.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='userid',
            field=models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.User'),
        ),
        migrations.AddField(
            model_name='address',
            name='userid',
            field=models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.User'),
        ),
    ]
