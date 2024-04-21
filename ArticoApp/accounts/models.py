from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.text import slugify

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models

from django.utils import timezone

from ArticoApp.products.models import MaxFileSizeValidator

# Create your models here.

# auth_models.AbstractUser

username_validator = UnicodeUsernameValidator()


class ArticoUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class ArticoUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # pasword and lastlogin from abstractBaseUser
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
        null=False
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


    profile_banner = models.ImageField(upload_to = 'profile_banner_photo/',
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
