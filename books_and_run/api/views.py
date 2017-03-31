from .serializers import (
    StatisticsCreateSerializer,
    StatisticsDetailSerializer,
    StatisticsListSerializer,
    StatisticsUpdateSerializer,
    )
from books_and_run.models import Statistics
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
Statistic views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class StatisticsCreateAPIView(CreateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsCreateSerializer
    #permission_classes = [IsAuthenticated]


class StatisticsDetailAPIView(RetrieveAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsDetailSerializer
    #permission_classes = [IsAuthenticated]


class StatisticsUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsUpdateSerializer
    # permission_classes = [IsAdminUser]


class StatisticsDeleteAPIView(DestroyAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsListSerializer
    permission_classes = [IsAdminUser]


class StatisticsListAPIView(ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsListSerializer
    #permission_classes = [IsAuthenticated]
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['player', 'game']
    # pagination_class = LimitOffsetPagination # PageNumberPagination
