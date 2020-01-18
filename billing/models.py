from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class BillingProfile(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    # Setting unique=True on a ForeignKey has the same effect as using a OneToOneField
    email       = models.EmailField(null=True, blank=True)
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


def user_created_reciver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)
post_save.connect(user_created_reciver, sender=User)