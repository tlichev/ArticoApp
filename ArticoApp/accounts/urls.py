from django.urls import path, include
from django.contrib.auth import  views as auth_views
from ArticoApp.accounts.views import SignInUserView, SignUpUserView, signout_user, \
    AuthorProfileView, AuthorProfileCreateView, follow_user

urlpatterns = (
    path('signup/', SignUpUserView.as_view(), name='signup-user'),
    path('signin/', SignInUserView.as_view(), name='signin-user'),
    path('signout/', signout_user, name='signout-user'),
    # path('author_profile/<int:pk>/', follow_user, name='follow-user', ),

    path('author_profile/<int:pk>/', include(
        [
        path('', AuthorProfileView.as_view(), name='author-profile'),
        path('create/', AuthorProfileCreateView.as_view(), name='author-profile-create'),

        path('like/', follow_user, name='follow-user', )


        ]
    )),

    # path('author_profile/<int:pk>/edit') to do edit profile view
)

