
from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from ArticoApp.accounts.forms import ProfileUserCreateForm, ArticoChangeForm


UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    add_form =ProfileUserCreateForm
    form = ArticoChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)
