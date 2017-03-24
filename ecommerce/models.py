from django.db import models
from django.utils.encoding import python_2_unicode_compatible

	
class Product(models.Model):
    ProductID = models.AutoField(db_column='ProductId', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    Price = models.TextField(db_column='Price', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    Image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
	
class User(models.Model):
    #userid = models.IntegerField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255)  # Field name made lowercase.

class Address(models.Model):
    addressid = models.AutoField(db_column='AddressId', primary_key=True)  # Field name made lowercase.
    addressline1 = models.CharField(db_column='AddressLine1', max_length=255)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='AddressLine2', max_length=255)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=255)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255)  # Field name made lowercase.
    userid = models.ForeignKey(User, db_column='UserId')  # Field name made lowercase.

class Paymentmethod(models.Model):
    paymentmethodid = models.AutoField(db_column='PaymentMethodId', primary_key=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=255)  # Field name made lowercase.
    expdate = models.CharField(db_column='ExpDate', max_length=255)  # Field name made lowercase.
    cardholdername = models.CharField(db_column='CardHolderName', max_length=255)  # Field name made lowercase.
    billingaddressid = models.ForeignKey(Address, db_column='BillingAddressId')  # Field name made lowercase.
    userid = models.ForeignKey(User, db_column='UserId')  # Field name made lowercase.

class Order(models.Model):
    orderid = models.AutoField(db_column='OrderId', primary_key=True)  # Field name made lowercase.
    confirmed = models.NullBooleanField(db_column='Confirmed')  # Field name made lowercase.
    date = models.DateField(db_column='date', null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='total', max_digits=7, decimal_places=2, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, db_column='UserId')  # Field name made lowercase.
    paymentmethodid = models.ForeignKey(Paymentmethod, db_column='PaymentMethodId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ManyToManyField(Product, db_column='ProductId')
