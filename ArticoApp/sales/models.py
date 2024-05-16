from django.db import models

from ArticoApp import settings
from ArticoApp.accounts.models import ArticoUser
from ArticoApp.products.models import Product


# Create your models here.

class Sale(models.Model):

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming currency
    shipping_address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(ArticoUser, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
