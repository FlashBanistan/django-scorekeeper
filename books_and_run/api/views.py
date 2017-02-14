from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView
    )
from books_and_run.models import Game
from .serializers import (
    GameCreateSerializer,
    GameDetailSerializer,
    GameListSerializer
    )


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
