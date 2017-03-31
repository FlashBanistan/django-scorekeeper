from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from books_and_run.models import Statistics
from accounts.api.serializers import UserDetailSerializer



"""
Statistics endpoints
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class StatisticsCreateSerializer(ModelSerializer):
    class Meta:
        model = Statistics
        fields = [
            'user',
            'games_won',
            'hands_won',
            'games_played',
            'high_score',
            'low_score',
        ]


class StatisticsDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Statistics
        fields = [
            'user',
            'games_won',
            'hands_won',
            'games_played',
            'high_score',
            'low_score',
        ]

class StatisticsUpdateSerializer(ModelSerializer):
    class Meta:
        model = Statistics
        fields = [
            'games_won',
            'hands_won',
            'games_played',
            'high_score',
            'low_score',
        ]


class StatisticsListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'books_and_run-api:statistics_detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Statistics
        fields = [
            'url',
            'user',
            'games_won',
            'hands_won',
            'games_played',
            'high_score',
            'low_score',
        ]
