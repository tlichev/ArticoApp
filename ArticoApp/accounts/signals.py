from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from ArticoApp.accounts.models import Profile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)

def user_created_signal(sender, instance, created, **kwargs):
    # created = False when update
    # created = True when create
    if not created:
        return
    Profile.objects.create(user=instance)