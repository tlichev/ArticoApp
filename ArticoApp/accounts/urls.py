from django.urls import path, include

from ArticoApp.accounts.views import register, login, show_author_profile

urlpatterns = (
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('author_profile/<slug:auth_slug>', include(
        [
        path('', show_author_profile, name='author-profile'),
    ]
    )),

    # path('author_profile/<int:pk>/edit') to do edit profile view
)

