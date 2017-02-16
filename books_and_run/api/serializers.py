from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
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
    winner = SerializerMethodField()
    class Meta:
        model = Game
        fields = [
            'id',
            'players',
            'winner',
            'created_on',
        ]

    def get_winner(self, obj):
        return str(obj.winner.username)


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
    player = SerializerMethodField()
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

    def get_player(self, obj):
        return str(obj.player.username)


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
