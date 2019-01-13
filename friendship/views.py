from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from friendship.models import FriendRequest, Friend
from friendship.serializers import FriendRequestSerializer, FriendSerializer

class FriendRequestViewSet(mixins.RetrieveModelMixin,
                        #    mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated,]

    @action(methods=['get'], detail=False)
    def received(self, request):
        qs = FriendRequest.objects.received_for_user(request.user)
        serializer = self.serializer_class(qs, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def sent(self, request):
        qs = FriendRequest.objects.sent_for_user(request.user)
        serializer = self.serializer_class(qs, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def accept(self, request, pk=None):
        FriendRequest.objects.accept_friend_request(request.user)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True)
    def reject(self, request, pk=None):
        FriendRequest.objects.reject_friend_request()
        return Response(status=status.HTTP_200_OK)


class FriendViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated,]

    """
    Override friend retrieve method so that a user can only get their own friends.
    """
    def retrieve(self, request, pk=None):
        friend = get_object_or_404(Friend.objects.for_user(request.user), pk=pk)
        serializer = self.get_serializer(friend)
        return Response(serializer.data)

    """
    Override the friends list view and filter for the requesting users friends.
    """
    def list(self, request):
        qs = Friend.objects.for_user(request.user)
        serializer = self.serializer_class(qs, many=True, context={'request': request})
        return Response(serializer.data)