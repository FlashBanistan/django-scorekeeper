from .serializers import FriendListDetailSerializer
from users.api.serializers import UserDetailSerializer
from ..models import FriendList
from rest_framework import viewsets
from scorekeeper.mixins import DefaultsMixin
from rest_framework.decorators import detail_route
from rest_framework.response import Response
import django_filters

class FriendFilter(django_filters.FilterSet):
    class Meta:
        model = FriendList
        fields = (
            'friends__username',
        )

class FriendListViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FriendList.objects.all()
    serializer_class = FriendListDetailSerializer
    filter_class = FriendFilter

    @detail_route(methods=['get'])
    def get_friend(self, request, pk=None):
        # print(dir(request.query_params))
        # print(request.query_params)
        queryset = self.get_queryset().get(pk=pk)
        friend = queryset.friends.get(username__icontains=request.query_params.get('username'))
        serialized_friend = UserDetailSerializer(friend, context={'request': request}).data


        return Response(serialized_friend)
