from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Member(models.Model):
    username = models.CharField(max_length=16,primary_key=True)
    email = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    house = models.CharField(max_length=16)
    address1 = models.CharField(max_length=16)
    address2 = models.CharField(max_length=16)
    postcode = models.CharField(max_length=16)
	
	
class Product(models.Model):
    ProductID = models.IntegerField(max_length=16,primary_key=True)
    Name = models.CharField(max_length=16)
    Price = models.CharField(max_length=16)
    Description = models.CharField(max_length=16)
	
class Basket(models.Model):
    StuffID_id = models.IntegerField(max_length=16)

