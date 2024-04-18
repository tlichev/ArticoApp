from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.
SIZE_5_MB = 5*1024*1024

# def image_size_less_that_5mb_validator(value):
#     if value.size >SIZE_5_MB:
#         raise ValidationError('The size of the image must be less than 5mb')


class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return max_size < file_size


class Product(models.Model):
    MAX_LENGTH = 300

    SLUG_MAX_LENGTH = 20

    name = models.CharField(
        max_length= MAX_LENGTH,
        null=False,
        blank=False
    )

    short_description = models.TextField()

    long_description = models.TextField()

    product_photo = models.ImageField(upload_to = 'product_photo/',
        null=False,
        blank=True,
        validators=(
        MaxFileSizeValidator(limit_value = SIZE_5_MB),
        )

    )

    likes = models.IntegerField(default=0)

    slug = models.SlugField(
        max_length=SLUG_MAX_LENGTH,
        unique=True, null=False,
        blank=True,
        editable= False,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now=True, #on every save

    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # 2 saves because by creating model id is none and slug id is equal none
        if not self.slug:
            self.slug = slugify(f'prod-{self.name}-{self.id}')
        super().save(*args, **kwargs)



class ProductLike(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)