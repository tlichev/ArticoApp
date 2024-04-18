from django.shortcuts import render, redirect

from ArticoApp.products.models import Product, ProductLike


# Create your views here.


def show_index(request):
    product_name_pattern = request.GET.get('product_name_pattern', None)

    products = Product.objects.all()


    if product_name_pattern:
        products = products.filter(product__name__icontains=product_name_pattern)

    context = {
        'product_photos': products,
        'product_name_pattern': product_name_pattern,
    }
    return render(request, 'index.html', context)

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

