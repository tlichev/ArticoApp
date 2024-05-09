from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from ArticoApp.accounts.forms import SignUpUserForm, ProfileUserCreateForm
from ArticoApp.accounts.models import Profile, ArticoUser, UserFollow
from ArticoApp.products.models import Product



# Create your views here.

# classes with call

class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True




class SignUpUserView(views.CreateView):
    template_name = "accounts/register.html"
    form_class = SignUpUserForm
    def get_success_url(self):
        return reverse_lazy('author-profile-create', kwargs={'pk': self.object.pk})

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
    queryset = Profile.objects.all()
    template_name = "product/author-profile.html"


class AuthorProfileCreateView(views.UpdateView):
    queryset = Profile.objects.all()


    form_class = ProfileUserCreateForm

    template_name = "accounts/create-profile-details.html"

    def get_success_url(self):
        return reverse('author-profile', kwargs={
            'pk': self.object.pk,
        })


#
# class AuthorProfileCreateView(views.UpdateView):
    queryset = Profile.objects.all()
#     template_name = "accounts/create-profile-details.html"
#     fields = ['username', 'first_name', 'last_name', 'bio', 'profile_photo', 'profile_banner', 'date_of_birth', ]
#
#     def get_success_url(self):
#         return reverse("author-profile", kwargs={
#             'pk': self.object.pk,
#         })
#
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class=form_class)
#
#         form.fields["date_of_birth"].widget.attrs["type"] = "date"
#         form.fields["date_of_birth"].label = "Birthday"
#         return form
#
#
#



def follow_user(request, pk):
    # product = Product.objects.get(pk=pk)

    user_follow = (UserFollow.objects
                    .filter(profile_id=pk)
                    .first())

    if user_follow:
        user_follow.delete()

    else:
        # like
        UserFollow.objects.create(profile_id = pk)

    return redirect(request.META.get('HTTP_REFERER') )
