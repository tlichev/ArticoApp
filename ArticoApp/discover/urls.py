from django.urls import path, include

from ArticoApp.discover.views import like_product, IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('dis/prod_like/<int:pk>/', like_product, name='product-like',)
)