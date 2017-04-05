from .serializers import (
    # StatisticsCreateSerializer,
    # StatisticsDetailSerializer,
    # StatisticsListSerializer,
    # StatisticsUpdateSerializer,
      StatisticsSerializer
    )
from books_and_run.models import Statistics
from rest_framework.filters import (
    DjangoFilterBackend,
    SearchFilter,
    OrderingFilter,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
import django_filters
from rest_framework.decorators import detail_route


"""
Statistic views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class StatisticsFilter(django_filters.FilterSet):

    class Meta:
        model = Statistics
        fields = ('games_won', 'hands_won', 'games_played', 'high_score', 'low_score')


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""

    # authentication_classes = JSONWebTokenAuthentication
    #
    # permission_classes = (
    #     IsAuthenticated,
    # )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )


class StatisticsViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    filter_class = StatisticsFilter
    search_fields = ('pk', 'user')
    ordering_fields = ('games_won', 'hands_won', 'games_played', 'high_score', 'low_score')

    def update(self, request, pk=None):
        stats = self.get_object()

        stats.increment_games_won(request.data['is_winner'])
        stats.add_to_hands_won(request.data['num_hands_won'])
        stats.increment_games_played()
        stats.new_low_score(request.data['score'])
        stats.new_high_score(request.data['score'])
        print("games_won: ", stats.games_won)
        print("hands_won: ", stats.hands_won)
        print("games_played: ", stats.games_played)
        print("high_score: ", stats.high_score)
        print("low_score: ", stats.low_score)

        serialized_stats = StatisticsSerializer(stats, context={'request': request}).data
        return Response(serialized_stats)

    @detail_route(methods=['patch'])
    def increment_games_played(self, request, pk=None):
        stats = self.get_object()
        stats.increment_games_played()
        stats.save()
        serializer = StatisticsSerializer(stats, context={'request': request}).data

        return Response(serializer)
