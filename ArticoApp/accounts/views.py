from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views, login,logout
from django.urls import reverse_lazy
from django.views import generic as views

from ArticoApp.accounts.forms import SignUpUserForm
from ArticoApp.accounts.models import Profile, ArticoUser
from ArticoApp.products.models import Product



# Create your views here.

# classes with call

class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True




class SignUpUserView(views.CreateView):
    template_name = "accounts/register.html"
    form_class = SignUpUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        result= super().form_valid(form)
        login(self.request, form.user)
        return result


def signout_user(request):
    logout(request)
    return render(request, 'index.html')


# def show_author_profile(request, auth_slug):
#     products = Product.objects.all()
#     context = {
#         'product_photos': products,
#     }
#
#     return render(request, 'product/author-profile.html', context)

class AuthorProfileView(views.DetailView):
    queryset = ArticoUser.objects.all()
    template_name = "product/author-profile.html"
    slug_url_kwarg = "auth_slug"




