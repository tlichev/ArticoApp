from django import forms

from ArticoApp.products.models import Product


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'copies', 'product_photo',  'price', 'short_description', 'long_description', ]

class ProductEditForm(ProductBaseForm):
    pass

class ProductCreateForm(ProductBaseForm):
    pass