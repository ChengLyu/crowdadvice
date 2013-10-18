from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    """Basic information for each user
    """
    user = models.OneToOneField(User, unique=True)
    current_location = models.TextField()
    birthday = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return str(self.user.id)


def create_profile(sender, instance, created, **kwargs):
    if created:
        (profile, created) = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_profile, sender=User)