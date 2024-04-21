from django.shortcuts import render, redirect

from ArticoApp.products.models import Product, ProductLike
from django.views import generic as views


# Create your views here.


# def show_index(request):
#     product_name_pattern = request.GET.get('product_name_pattern', None)
#
#     products = Product.objects.all()
#
#
#     if product_name_pattern:
#         products = products.filter(product__name__icontains=product_name_pattern)
#
#     context = {
#         'product_photos': products,
#         'product_name_pattern': product_name_pattern,
#     }
#     return render(request, 'index.html', context)

class IndexView(views.ListView):
    queryset = Product.objects.all()

    template_name = 'index.html'

    @property
    def product_name_pattern(self):
        return self.request.GET.get('product_name_pattern', None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['product_name_pattern'] = self.product_name_pattern

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_product_by_name(queryset)
        return queryset

    def filter_product_by_name(self, queryset):
        product_name_pattern = self.product_name_pattern

        filter_query = {}

        if product_name_pattern:
            filter_query['product__name__icontains'] = product_name_pattern

        if product_name_pattern:
            return queryset.filter(**filter_query)
        return queryset






def like_product(request, pk):
    # product = Product.objects.get(pk=pk)

    product_like = (ProductLike.objects
                    .filter(product_id=pk)
                    .first())

    if product_like:
        product_like.delete()

    else:
        # like
        ProductLike.objects.create(product_id = pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#prod-{pk}")

