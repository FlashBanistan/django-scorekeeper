from .serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

User = get_user_model()



"""
Account views
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    # permission_classes = [AllowAny]
    query_set = User.objects.all()
