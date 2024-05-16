from ArticoApp.discounts.models import Discount
from django import forms

from ArticoApp.sales.models import Sale


class SaleCreateForm(forms.ModelForm):
    class Meta:
        model = Sale

        fields = ['quantity']

