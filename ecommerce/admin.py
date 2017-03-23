from django.contrib import admin
from .models import Product, User, Address, Paymentmethod, Order

@admin.register(Product, User, Address, Paymentmethod, Order)
class PersonAdmin(admin.ModelAdmin):
    pass
