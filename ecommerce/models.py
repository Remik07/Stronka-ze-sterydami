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
	
	
class Records(models.Model):
    capital = models.FloatField(max_length=200)
    years = models.FloatField(max_length=200)
    rate = models.FloatField(max_length=200)
    amount = models.FloatField(max_length=200)

