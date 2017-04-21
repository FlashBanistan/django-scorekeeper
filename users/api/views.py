from .serializers import (
    UserCreateSerializer,
    # UserLoginSerializer,
    FriendListCreateSerializer,
    FriendListDetailSerializer
    )
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
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
from users.models import FriendList

User = get_user_model()

"""
Account views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    query_set = User.objects.all()


# class UserLoginAPIView(APIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = [AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = UserLoginSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             new_data = serializer.data
#             return Response(new_data, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


"""
FriendList views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class FriendListCreateAPIView(CreateAPIView):
    queryset = FriendList.objects.all()
    serializer_class = FriendListCreateSerializer
    #permission_classes = [IsAuthenticated]


class FriendListDetailAPIView(RetrieveAPIView):
    queryset = FriendList.objects.all()
    serializer_class = FriendListDetailSerializer
