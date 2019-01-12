from django.db import models
from rest_framework.exceptions import ValidationError
from django.conf import settings


class FriendshipRequestManager(models.Manager):
    pass

class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friend_requests_received', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = FriendshipRequestManager()

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        # pylint: disable=no-member
        return f'User {self.from_user_id} is friends with {self.to_user_id}.'

    def save(self, *args, **kwargs):
        if self.from_user == self.to_user:
            raise ValidationError("Users cannot be friends with themselves.")
        super(FriendshipRequest, self).save(*args, **kwargs)