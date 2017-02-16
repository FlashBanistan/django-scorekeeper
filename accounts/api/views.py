from .serializers import (
    UserCreateSerializer,
    )
from django.contrib.auth import get_user_model
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

User = get_user_model()

"""
Account views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    query_set = User.objects.all()
