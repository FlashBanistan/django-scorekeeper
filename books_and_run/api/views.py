from .serializers import (
    GameCreateSerializer,
    GameDetailSerializer,
    GameListSerializer,
    ScoreCreateSerializer,
    ScoreDetailSerializer,
    ScoreListSerializer,
    )
from books_and_run.models import Game, Score
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.filters import (
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



"""
Game views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class GameCreateAPIView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer
    permission_classes = [IsAuthenticated]


class GameDetailAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer


class GameUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class GameDeleteAPIView(DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['winner']
    pagination_class = LimitOffsetPagination # PageNumberPagination


"""
Score views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class ScoreCreateAPIView(CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreCreateSerializer


class ScoreDetailAPIView(RetrieveAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreDetailSerializer


class ScoreUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ScoreDeleteAPIView(DestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ScoreListAPIView(ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['player', 'game']
    pagination_class = LimitOffsetPagination # PageNumberPagination
