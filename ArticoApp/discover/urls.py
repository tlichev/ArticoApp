from django.urls import path, include

from ArticoApp.discover.views import IndexView, DiscoverView, DiscountsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('discover/', DiscoverView.as_view(), name='discover'),
    path('discounts/', DiscountsView.as_view(), name='discounts'),
)