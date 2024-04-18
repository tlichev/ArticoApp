from django.shortcuts import render, redirect
from django.urls import reverse

from ArticoApp.products.forms import ProductCreateForm, ProductBaseForm
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin


# Create your views here.

def create_product(request):
    product_create_form = ProductCreateForm(request.POST or None)

    if request.method == 'POST':
        if product_create_form.is_valid():
            product_create_form.save()
            return redirect('index')
    context = {
        'product_form': product_create_form,
    }

    return render(request, 'forms/create-product-form.html', context)


# class ProductCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
#
#
#     form_class = ProductBaseForm
#     template_name = "forms/create-product-form.html"
#
#     def get_success_url(self):
#         return reverse("index", kwargs={
#             "username": self.object.user.email,
#             "product_slug": self.object.slug,
#         })
#
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class=form_class)
#
#         form.instance.user = self.request.user
#         return form