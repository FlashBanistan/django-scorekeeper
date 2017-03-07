from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from books_and_run.models import (
    Game,
    Score,
    Statistics,
)
from accounts.api.serializers import UserDetailSerializer



"""
Game endpoints
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class GameCreateSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'players',
        ]


class GameDetailSerializer(ModelSerializer):
    winner = UserDetailSerializer(read_only=True)
    players = UserDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Game
        fields = [
            'id',
            'players',
            'winner',
            'created_on',
        ]


class GameListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'books_and_run-api:game_detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Game
        fields = [
            'url',
            'id',
            'players',
            'winner',
            'created_on',
        ]



"""
Score endpoints
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class ScoreCreateSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = [
            'player',
            'game',
            'created_on',
            'round_one',
            'round_two',
            'round_three',
            'round_four',
            'round_five',
            'round_six',
            'round_seven',
        ]


class ScoreDetailSerializer(ModelSerializer):
    player = UserDetailSerializer(read_only=True)
    class Meta:
        model = Score
        fields = [
            'id',
            'player',
            'game',
            'created_on',
            'round_one',
            'round_two',
            'round_three',
            'round_four',
            'round_five',
            'round_six',
            'round_seven',
        ]


class ScoreListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'books_and_run-api:score_detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Score
        fields = [
            'url',
            'id',
            'player',
            'game',
            'created_on',
            'round_one',
            'round_two',
            'round_three',
            'round_four',
            'round_five',
            'round_six',
            'round_seven',
        ]



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
