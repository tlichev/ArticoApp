from django.urls import path, include

from ArticoApp.discover.views import  IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)