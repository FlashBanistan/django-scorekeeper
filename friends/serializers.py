from .models import FriendList
from users.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer


class FriendListCreateSerializer(ModelSerializer):
    class Meta:
        model = FriendList
        fields = [
            'user',
            'friends',
        ]


class FriendListDetailSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    friends = UserSerializer(many=True, read_only=True)
    class Meta:
        model = FriendList
        fields = [
            'user',
            'friends',
        ]
