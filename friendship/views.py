from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from friendship.models import FriendRequest, Friend
from friendship.serializers import FriendRequestSerializer, FriendSerializer


class FriendRequestViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated,]

    @action(methods=['get'], detail=False)
    def recieved(self, request):
        queryset = self.get_queryset().filter(to_user=self.request.user)
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def sent(self, request):
        queryset = self.get_queryset().filter(from_user=self.request.user)
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def accept(self, request, pk=None):
        fr = FriendRequest.objects.get(pk=pk)
        fr.accept()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True)
    def reject(self, request, pk=None):
        fr = FriendRequest.objects.get(pk=pk)
        fr.reject()
        return Response(status=status.HTTP_200_OK)


class FriendViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated,]