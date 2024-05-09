from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ArticoApp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ArticoApp.discover.urls')),
    path('a/', include('ArticoApp.accounts.urls')),
    path('products/', include('ArticoApp.products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
