
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now

from ArticoApp.discounts.forms import DiscountCreateForm
from django.views import generic as views

from ArticoApp.discounts.models import Discount
from ArticoApp.products.models import Product
from django.utils import timezone



class DiscountCreateView(views.CreateView):

    form_class = DiscountCreateForm

    template_name = "discounts/discount-create-form.html"




    def get_success_url(self):
        return reverse_lazy('details-product', kwargs={'username': self.request.user.email,
                                                       'product_slug':self.kwargs['product_slug']})
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        slug = self.kwargs['product_slug']

        product = Product.objects.get(slug=slug)

        form.instance.product = product



        return form


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['product_slug']

        product = Product.objects.get(slug=slug)

        context.update({
            'product': product,

        })

        return context



    def form_valid(self, form) -> DiscountCreateForm:
        discount = form.instance
        if discount.discount_percentage is not None:
            discount.price_with_discount = discount.product.price * (1 - (discount.discount_percentage / 100))


        return super().form_valid(form)


