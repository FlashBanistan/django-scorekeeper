from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from scorekeeper.mixins import DefaultsMixin
from users.serializers import UserSerializer

User = get_user_model()

class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_class = StatisticsFilter
    # search_fields = ('pk', 'user')
    # ordering_fields = (
    #     'games_won',
    #     'hands_won',
    #     'games_played',
    #     'high_score',
    #     'low_score',
    # )