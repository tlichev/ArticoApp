import random

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from ArticoApp.accounts.models import Profile
from ArticoApp.products.models import Product
from django.views import generic as views, View
from django.db.models import Count


UserModel = get_user_model()



class IndexView(views.ListView):
    queryset = Product.objects.all()



    def get_template_names(self):
        if self.request.user.is_authenticated:
            # User is authenticated
            return ['discover/index-user.html']
        else:
            # User is not authenticated
            return ['discover/index.html']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:

            products = Product.objects.order_by('?')[:10]

            first_product = Product.objects.order_by('name').first()
            second_product = Product.objects.order_by('id').first()


            context.update({
                'products': products,
                'first_product': first_product,
                'second_product': second_product,
            })
        else:

            products = Product.objects.order_by('?')[:10]
            user_products = Product.objects.filter(user=self.request.user)

            top_sellers = Profile.objects.order_by('user_id')[:10]

            top_authors = Profile.objects.order_by('user_id')[:4]



            # sort_top_authors(top_authors)


            context.update({
                'products': products,
                'user_products': user_products,
                'top_sellers': top_sellers,
                'top_authors': top_authors,
            })

        return context


# def index_view(request):
#     if not request.user.is_authenticated:
#         product_name_pattern = request.GET.get('product_name_pattern', None)
#
#
#
#         products = Product.objects.order_by('?')[:10]
#
#         first_product = Product.objects.order_by('name').first()
#         second_product = Product.objects.order_by('id').first()
#
#
#         if product_name_pattern:
#             products = products.filter(product__name__icontains=product_name_pattern)
#
#         context = {
#             'products': products,
#             'product_name_pattern': product_name_pattern,
#             'first_product': first_product,
#             'second_product': second_product,
#         }
#         return render(request, 'discover/index.html', context)
#     else:
#
#         return render(request, 'discover/index-user.html')

# class IndexViewWithoutUser(View):
#     template_name = 'discover/index.html'
#
#     def get(self, request):
#         product_name_pattern = request.GET.get('product_name_pattern', None)
#
#         products = Product.objects.order_by('?')[:10]
#         first_product = Product.objects.order_by('name').first()
#         second_product = Product.objects.order_by('id').first()
#
#         if product_name_pattern:
#             products = products.filter(name__icontains=product_name_pattern)
#
#         context = {
#             'products': products,
#             'product_name_pattern': product_name_pattern,
#             'first_product': first_product,
#             'second_product': second_product,
#         }
#         return render(request, self.template_name, context)
#
# class IndexViewWithUser(View):
#     template_name = 'discover/index.html'

    # def get(self, request):
    #     product_name_pattern = request.GET.get('product_name_pattern', None)
    #
    #     products = Product.objects.order_by('?')[:10]
    #     first_product = Product.objects.order_by('name').first()
    #     second_product = Product.objects.order_by('id').first()
    #
    #     if product_name_pattern:
    #         products = products.filter(name__icontains=product_name_pattern)
    #
    #     context = {
    #         'products': products,
    #         'product_name_pattern': product_name_pattern,
    #         'first_product': first_product,
    #         'second_product': second_product,
    #     }
    #     return render(request, self.template_name, context)




















# Create your views here.


# def show_index(request):
#     product_name_pattern = request.GET.get('product_name_pattern', None)
#
#
#
#     products = Product.objects.order_by('?')[:10]
#
#     first_product = Product.objects.order_by('name').first()
#     second_product = Product.objects.order_by('id').first()
#
#
#     if product_name_pattern:
#         products = products.filter(product__name__icontains=product_name_pattern)
#
#     context = {
#         'products': products,
#         'product_name_pattern': product_name_pattern,
#         'first_product': first_product,
#         'second_product': second_product,
#     }
#     return render(request, 'discover/index.html', context)

# class IndexView(views.ListView):
#     template_name = 'index.html'
#     context_object_name = 'products'
#     queryset = Product.objects.order_by('?')[:3]
#
#
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#
#     first_product = Product.objects.order_by('name').first()
#
#
#     # Add the alphabetical product to the context
#     context['products'] = self.queryset
#     context['first_product'] = first_product
#
#     return context
#
#


