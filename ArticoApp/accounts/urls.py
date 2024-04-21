from django.urls import path, include
from django.contrib.auth import  views as auth_views
from ArticoApp.accounts.views import SignInUserView, SignUpUserView, signout_user, \
    AuthorProfileView

urlpatterns = (
    path('signup/', SignUpUserView.as_view(), name='signup-user'),
    path('signin/', SignInUserView.as_view(), name='signin-user'),
    path('signout/', signout_user, name='signout-user'),
    path('<slug:auth_slug>', include(
        [
        path('', AuthorProfileView.as_view(), name='author-profile'),
    ]
    )),

    # path('author_profile/<int:pk>/edit') to do edit profile view
)

