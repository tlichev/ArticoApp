import random

from django.contrib.auth import get_user_model


from ArticoApp.accounts.models import Profile
from ArticoApp.discounts.models import Discount
from ArticoApp.products.models import Product
from django.views import generic as views, View


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


            all_products = Product.objects.all()
            products_with_discount = []
            products_without_discount = []

            if all_products:
                for product in all_products:
                    if Discount.objects.filter(product_id=product.pk):
                        products_with_discount.append(product)
                    else:
                        products_without_discount.append(product)

            first_product = products_with_discount[0]
            second_product = products_without_discount[0]



            context.update({
                'products': all_products,
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


class DiscoverView(views.ListView):
    queryset = Product.objects.all()
    template_name = 'discover/discover-1.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()

        context.update({
            'products': products,

        })

        return context

class DiscountsView(views.ListView):
    queryset = Product.objects.all()
    template_name = 'discover/discounts-products.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_products = Product.objects.all()

        products_with_discount = []

        if all_products:
            for product in all_products:
                if Discount.objects.filter(product_id=product.pk):
                    products_with_discount.append(product)


        context.update({
            'products_with_discount': products_with_discount,
        })

        return context




