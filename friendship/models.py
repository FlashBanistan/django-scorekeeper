from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from django.conf import settings


class FriendRequestManager(models.Manager):
    def received_for_user(self, user):
        return FriendRequest.objects.filter(to_user=user)

    def sent_for_user(self, user):
        return FriendRequest.objects.filter(from_user=user)

    def send_friend_request(self, from_user, to_user):

        # Check if friendship already exists:
        already_friends = Friend.objects.filter(from_user=from_user, to_user=to_user).exists()
        if already_friends:
            raise ValidationError("Friendship already exists")
        
        # Check if friend request has already been sent:
        request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
        if created is False:
            raise ValidationError("Friendship already requested")

        return request

    def accept_friend_request(self, requesting_user):
        fr = self.get()
        # Validate that the friend request is being accepted by the person it was sent to:
        if fr.to_user != requesting_user:
            raise ValidationError("Only the user to whom this request was sent can accept it.")
        
        # Create the friendship:
        Friend.objects.create(from_user=fr.from_user, to_user=fr.to_user)
        Friend.objects.create(from_user=fr.to_user, to_user=fr.from_user)

        # Delete the friend request:
        fr.delete()

        # Delete any reverse requests:
        FriendRequest.objects.filter(from_user=fr.to_user, to_user=fr.from_user).delete()

        return True

    def reject_friend_request(self):
        fr = self.get()
        fr.delete()

        return True
        


class FriendRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friend_requests_received', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = FriendRequestManager()

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        # pylint: disable=no-member
        return f'User {self.from_user_id} requests to be friends with {self.to_user_id}.'

    def save(self, *args, **kwargs):
        if self.from_user == self.to_user:
            raise ValidationError("Users cannot be friends with themselves.")
        super(FriendRequest, self).save(*args, **kwargs)


class FriendManager(models.Manager):
    def for_user(self, user):
        return Friend.objects.filter(to_user=user)


class Friend(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friends', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    objects = FriendManager()

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        # pylint: disable=no-member
        return f'User {self.from_user_id} is friends with {self.to_user_id}.'

    def save(self, *args, **kwargs):
        if self.from_user == self.to_user:
            raise ValidationError("Users cannot be friends with themselves.")
        super(Friend, self).save(*args, **kwargs)