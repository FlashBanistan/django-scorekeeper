from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView
    )
from books_and_run.models import Game, Score
from .serializers import (
    GameCreateSerializer,
    GameDetailSerializer,
    GameListSerializer,
    ScoreCreateSerializer,
    ScoreDetailSerializer,
    ScoreListSerializer,
    )


"""
Game views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class GameCreateAPIView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer


class GameDetailAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer


class GameUpdateAPIView(UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


class GameDeleteAPIView(DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


"""
Score views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class ScoreCreateAPIView(CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreCreateSerializer


class ScoreDetailAPIView(RetrieveAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreDetailSerializer


class ScoreUpdateAPIView(UpdateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreListSerializer


class ScoreDeleteAPIView(DestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreListSerializer


class ScoreListAPIView(ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreListSerializer
