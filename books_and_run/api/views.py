from scorekeeper.mixins import DefaultsMixin
from .serializers import StatisticsSerializer
from books_and_run.models import Statistics
from rest_framework import viewsets
from rest_framework.response import Response
import django_filters
from rest_framework.exceptions import ParseError



class StatisticsFilter(django_filters.FilterSet):

    class Meta:
        model = Statistics
        fields = (
            'games_won',
            'hands_won',
            'games_played',
            'high_score',
            'low_score',
        )


class StatisticsViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    filter_class = StatisticsFilter
    search_fields = ('pk', 'user')
    ordering_fields = (
        'games_won',
        'hands_won',
        'games_played',
        'high_score',
        'low_score',
    )

    """
    Override the http PUT action to accept and handle the following parameters:
        'is_winner',
        'num_hands_won',
        'score'.
    """
    def update(self, request, *args, **kwargs):
        # Check the request for correct data:
        try:
            request.data['is_winner']
            request.data['num_hands_won']
            request.data['score']
        except KeyError as e:
            raise ParseError(detail="Missing key: " + str(e))

        # Handle the request:
        stats = self.get_object()
        stats.increment_games_won(request.data['is_winner'])
        stats.add_to_hands_won(request.data['num_hands_won'])
        stats.increment_games_played()
        stats.new_low_score(request.data['score'])
        stats.new_high_score(request.data['score'])
        stats.save()
        serialized_stats = StatisticsSerializer(stats, context={'request': request}).data

        return Response(serialized_stats)
