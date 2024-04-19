from django.urls import path, include

from ArticoApp.discover.views import show_index, like_product

urlpatterns = (
    path('dis/', show_index, name='index'),
    path('dis/prod_like/<int:pk>/', like_product, name='product-like',)
)