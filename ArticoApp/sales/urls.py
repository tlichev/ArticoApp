from django.urls import path, include

from ArticoApp.sales.views import sale_product, SaleCreateView, checkout, CheckoutView

urlpatterns = (
    # path('', sale_product, name='sale-product'),
    path('<str:username>/<slug:product_slug>/', SaleCreateView.as_view(), name='sale-product'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
)