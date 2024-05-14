from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.text import slugify

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models, get_user_model

from django.utils import timezone

from ArticoApp.accounts.managers import ArticoUserManager
from ArticoApp.products.models import MaxFileSizeValidator


# Create your models here.

# auth_models.AbstractUser

username_validator = UnicodeUsernameValidator()





class ArticoUser(AbstractBaseUser, auth_models.PermissionsMixin):
    SLUG_MAX_LENGTH = 50


    email = models.EmailField(
        _("email"),
        max_length=150,
        unique=True,

        validators=[username_validator],
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    slug = models.SlugField(
        max_length=SLUG_MAX_LENGTH,
        unique=True, null=False,
        blank=True,
        editable= False,
    )

    USERNAME_FIELD = "email"

    objects = ArticoUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # 2 saves because by creating model id is none and slug id is equal none
        if not self.slug:
            self.slug = slugify(f'author-{self.id}')
        super().save(*args, **kwargs)



class Profile(models.Model):
    SIZE_3_MB = 3 * 1024 * 1024

    MAX_USERNAME_LENGTH = 64
    MAX_FIRST_NAME_LENGTH = 30
    MAX_lAST_NAME_LENGTH = 50

    username = models.CharField(
        max_length= 64,
        blank=True,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    bio = models.TextField(
        blank=True,
        null=True
       )


    profile_photo = models.ImageField(upload_to = 'profile_photo/',
        null=False,
        blank=False,
        validators=(
        MaxFileSizeValidator(limit_value = SIZE_3_MB),
        )


    )


    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    user = models.OneToOneField(
        ArticoUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )


class UserFollow(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)