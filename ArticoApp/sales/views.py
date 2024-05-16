from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView

from ArticoApp.accounts.models import ArticoUser
from ArticoApp.discounts.forms import DiscountCreateForm
from django.views import generic as views

from ArticoApp.discounts.models import Discount
from ArticoApp.products.models import Product
from ArticoApp.sales.forms import SaleCreateForm
from ArticoApp.sales.models import Sale
from datetime import datetime, timedelta


def sale_product(request):
    return render(request, 'sales/buy-card-page.html')






class SaleCreateView(views.CreateView):

    form_class = SaleCreateForm

    template_name = "sales/buy-card-page.html"




    def get_success_url(self):
        return reverse_lazy('details-product', kwargs={'username': self.kwargs['username'],
                                                       'product_slug':self.kwargs['product_slug']})
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        username = self.kwargs['username']
        slug = self.kwargs['product_slug']

        user = ArticoUser.objects.get(email=username)
        product = Product.objects.get(slug=slug)


        form.instance.product = product
        form.instance.owner = user
        form.instance.price = 10

        return form


    def form_valid(self, form) -> SaleCreateForm:
        sale = form.instance
        product = Product.objects.filter(slug=self.kwargs['product_slug']).first()
        discount = Discount.objects.filter(product_id=product.pk).first()
        print(f'{product} {discount}')

        if sale.quantity > product.copies:
            return HttpResponseRedirect(reverse('index'))
            # raise ValidationError("Sale quantity exceeds available copies of the product.")

        if discount is not None :
            sale.price = sale.quantity*discount.price_with_discount
            product.copies -= sale.quantity
            product.save()
        else:
            sale.price = sale.quantity*product.price
            product.copies -= sale.quantity
            product.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('index'))



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']
        slug = self.kwargs['product_slug']

        context.update({
            'username': username,
            'slug': slug,

        })

        return context


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'sales/checkout-sales.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the current user (owner)
        owner = self.request.user

        # Get the first day of the current month
        current_date = datetime.now()
        first_day_of_current_month = current_date.replace(day=1)

        # Get the last day of the previous month
        last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)

        # Filter sales for the previous month for the owner
        sales = Sale.objects.filter(
            owner=owner,
        )

        # Calculate total revenue for the previous month
        total_revenue_previous_month = sales.aggregate(total_revenue=Sum('price'))['total_revenue']

        # If there are no sales, set total revenue to zero
        if total_revenue_previous_month is None:
            total_revenue_previous_month = 0

        count_of_products = len(sales)

        context['sales'] = sales
        context['count_of_products'] = count_of_products
        context['total_revenue_previous_month'] = total_revenue_previous_month

        return context


def checkout(request):
    return render(request, 'sales/checkout-sales.html')