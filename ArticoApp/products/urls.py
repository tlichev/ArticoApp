from django.urls import path, include

from ArticoApp.products.views import ProductCreateView, ProductDetailView, like_product

urlpatterns = (
    path('c/', ProductCreateView.as_view(), name='create-product'),
    path('dis/prod_like/<int:pk>/', like_product, name='product-like'),

    path("<str:username>/<slug:product_slug>/",
             include([
                 path("", ProductDetailView.as_view(), name='details-product'),
                 # path("edit/", PetEditView.as_view(), name='edit pet'),
                 # path("delete/", PetDeleteView.as_view(), name='delete pet'),
             ])),
)