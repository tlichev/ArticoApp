from ArticoApp.discounts.models import Discount
from django import forms


class DiscountCreateForm(forms.ModelForm):
    class Meta:
        model = Discount

        fields = ['discount_event_name', 'discount_percentage',  'discount_end_date']

        widgets = {


            "discount_end_date": forms.DateInput(attrs={
                'class': 'date-input',
                'placeholder': 'YYYY-MM-DD',
                'type': 'date'
            }),

        }
