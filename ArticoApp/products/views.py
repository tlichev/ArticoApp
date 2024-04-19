from django.shortcuts import render, redirect
from django.urls import reverse

from ArticoApp.products.forms import ProductCreateForm, ProductBaseForm
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from ArticoApp.products.models import Product


# Create your views here.

# def create_product(request):
#     product_create_form = ProductCreateForm(request.POST or None)
#
#     if request.method == 'POST':
#         if product_create_form.is_valid():
#             product_create_form.save()
#             return redirect('index')
#     context = {
#         'product_form': product_create_form,
#     }
#
#     return render(request, 'forms/create-product-form.html', context)


class ProductCreateView(views.CreateView):


    form_class = ProductCreateForm

    template_name = "product/create-product-form.html"

    def get_success_url(self):
        return reverse('details-product', kwargs={
            'username': 'vic',
            'product_slug': self.object.slug,
        })

class ProductDetailView(views.DetailView):
    model = Product
    template_name = "product/item-details.html"
    slug_url_kwarg = "product_slug"


