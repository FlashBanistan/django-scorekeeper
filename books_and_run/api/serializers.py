from rest_framework.serializers import ModelSerializer
from books_and_run.models import (
    Game,
    Score,
)


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
    class Meta:
        model = Game
        fields = [
            'id',
            'players',
            'winner',
            'created_on',
        ]
