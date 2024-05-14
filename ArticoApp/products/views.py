from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse

from ArticoApp.products.forms import ProductCreateForm, ProductBaseForm
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin, get_user_model

from ArticoApp.products.models import Product, ProductLike


class OwnerRequiredMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset= queryset)

        if not self.request.user.is_authenticated or obj.user != self.request.user:
            raise PermissionDenied

        return obj



class ProductCreateView(views.CreateView, auth_mixin.LoginRequiredMixin):


    form_class = ProductCreateForm

    template_name = "product/create-product-form.html"

    def get_success_url(self):
        return reverse('details-product', kwargs={
            'username': self.object.user.email,
            'product_slug': self.object.slug,
        })

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form

class ProductDetailView(views.DetailView, auth_mixin.LoginRequiredMixin):
    queryset = Product.objects.all().prefetch_related('productlike_set')
    template_name = "product/item-details.html"
    slug_url_kwarg = "product_slug"


# views.py


def like_product(request, pk):
    # product = Product.objects.get(pk=pk)

    product_like = (ProductLike.objects
                    .filter(product_id=pk,user_id=request.user.id)
                    .first())

    if product_like:
        product_like.delete()

    else:
        # like
        ProductLike.objects.create(product_id = pk,user_id=request.user.id)

    return redirect(request.META.get('HTTP_REFERER') + f"#prod-{pk}")


