from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from ArticoApp.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ('')
    pass
