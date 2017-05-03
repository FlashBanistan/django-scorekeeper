from .serializers import FriendListDetailSerializer
from users.api.serializers import UserDetailSerializer
from ..models import FriendList
from rest_framework import viewsets
from scorekeeper.mixins import DefaultsMixin
from rest_framework.decorators import detail_route
from rest_framework.response import Response



class FriendListViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FriendList.objects.all()
    serializer_class = FriendListDetailSerializer

    @detail_route(methods=['get'])
    def get_friend(self, request, pk=None):
        friends = self.get_queryset().get(pk=pk).friends.filter(username__icontains=request.query_params.get('username'))
        serialized_friends = UserDetailSerializer(friends, many=True, context={'request': request}).data

        return Response(serialized_friends)
