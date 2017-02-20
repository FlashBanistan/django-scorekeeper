from django.db import models
from django.contrib.auth.models import User


class FriendList(models.Model):
    # Define model fields:
    user = models.OneToOneField(User)
    friends = models.ManyToManyField(User, related_name='friends')

    def __str__(self):
        return str(self.pk)
