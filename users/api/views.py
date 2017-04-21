from .serializers import (
    UserCreateSerializer,
    FriendListDetailSerializer
    )
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.generics import (
    CreateAPIView,
    )
from users.models import FriendList
from rest_framework import viewsets
from scorekeeper.mixins import DefaultsMixin



"""
Account views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    # permission_classes = [AllowAny]
    query_set = User.objects.all()


"""
FriendList views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class FriendListViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FriendList.objects.all()
    serializer_class = FriendListDetailSerializer
    # filter_class = asdf
