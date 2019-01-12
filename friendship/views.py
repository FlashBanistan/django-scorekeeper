from rest_framework import viewsets
from friendship.models import FriendshipRequest
from friendship.serializers import FriendshipRequestSerializer


class FriendshipRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer