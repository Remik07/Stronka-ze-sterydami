from django.contrib import admin
from .models import Member, Product, Basket

@admin.register(Member, Product, Basket)
class PersonAdmin(admin.ModelAdmin):
    pass