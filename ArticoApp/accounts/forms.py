from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from ArticoApp.accounts.models import ArticoUser, Profile

UserModel = get_user_model()


class SignUpUserForm(auth_forms.UserCreationForm):
    user = None
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

    def save(self, *args, **kwargs):
        self.user = super().save(*args,**kwargs)
        return self.user


class ProfileUserCreateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['username', 'first_name',  'last_name', 'bio', 'profile_photo','profile_banner', 'date_of_birth',]




