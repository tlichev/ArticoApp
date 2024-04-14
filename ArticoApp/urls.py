
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('ArticoApp.discover.urls')),
    path('authors/', include('ArticoApp.accounts.urls')),
    path('products/', include('ArticoApp.products.urls')),
    path('photos/', include('ArticoApp.photos.urls')),
)
