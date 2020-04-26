from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, null=False)
    contact_no = models.CharField(null=True, max_length=13)
    email = models.EmailField(null=False, blank=False)
    active = models.BooleanField(default=True, null=False)
    is_restaurant = models.BooleanField(default=False, null=False)
    is_customer = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


