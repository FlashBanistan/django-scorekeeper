from .serializers import FriendListDetailSerializer
from ..models import FriendList
from rest_framework import viewsets
from scorekeeper.mixins import DefaultsMixin



class FriendListViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FriendList.objects.all()
    serializer_class = FriendListDetailSerializer
    # filter_class = asdf
