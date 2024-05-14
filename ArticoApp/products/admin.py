from django.contrib import admin

from ArticoApp.products.models import Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass