from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class FriendList(models.Model):
    # Define model fields:
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friends')

    def __str__(self):
        return str(self.pk)

    # Listen for user activity.
    @receiver(post_save, sender=User)
    # When a user is created, this will attach a friendlist to the user.
    def create_friendlist(sender, instance, created, **kwargs):
        if created:
            FriendList.objects.create(user=instance)
