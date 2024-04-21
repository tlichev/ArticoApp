from django.contrib.auth import forms as auth_forms, get_user_model

from ArticoApp.accounts.models import ArticoUser

UserModel = get_user_model()


class SignUpUserForm(auth_forms.UserCreationForm):
    user = None
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

    def save(self, *args, **kwargs):
        self.user = super().save(*args,**kwargs)
        return self.user




