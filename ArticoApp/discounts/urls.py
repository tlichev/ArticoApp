from django.urls import path, include

from ArticoApp.discounts.views import DiscountCreateView

urlpatterns = (
    path("create/<slug:product_slug>/", DiscountCreateView.as_view(), name="create-product-discount"),
)