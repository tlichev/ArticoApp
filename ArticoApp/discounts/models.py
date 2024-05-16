from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

from ArticoApp.products.models import Product


class Discount(models.Model):
    MAX_LENGTH = 300
    discount_event_name = models.CharField(
        max_length=MAX_LENGTH,
       null=True,
       blank=False
       )

    price_with_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null= True,
        blank= True,

      )

    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )


    discount_end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='discounts')



    def check_active_status(self):
        now = timezone.now()
        if self.discount_end_date < now:
            self.is_active = False
            self.save()
        else:
            self.is_active = True
            self.save()

    def set_price_with_discount(self):
        self.price_with_discount = self.product.price * (1 - (self.discount_percentage / 100))
        self.save()


    def __str__(self):
        return f"{self.discount_percentage}% off on {self.product.name}"
