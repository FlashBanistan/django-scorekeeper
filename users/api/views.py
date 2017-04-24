from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UserDetailSerializer
from scorekeeper.mixins import DefaultsMixin

User = get_user_model()



class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
