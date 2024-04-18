from django.urls import path

from ArticoApp.products.views import create_product

urlpatterns = (
    path('c/', create_product, name='create product'),
)