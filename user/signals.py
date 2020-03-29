from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from user.models import Profile

# When a user is saved, send a signal.
# The signal is going to be received by the receiver.
# The receiver is "create_profile" function.
# The receiver will create a new profile with the new user.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# The receiver will save the new profile to the datebase
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
