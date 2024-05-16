from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from ArticoApp.accounts.models import Profile

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

        fields = ['username', 'first_name',  'last_name', 'bio', 'profile_photo', 'date_of_birth',]

        widgets = {

            "date_of_birth": forms.DateInput(attrs={
                'class': 'date-input',
                'placeholder': 'YYYY-MM-DD',
                'type': 'date'
            }),

        }




class ArticoChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel