from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from books_and_run.models import (
    Game,
    Score,
)

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
        view_name = 'books_and_run-api:game_detail',
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
