from django.conf import settings
from django.db import models


class IHaveUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    class Meta:
        abstract = True