from ..models import FriendList
from users.api.serializers import UserListSerializer, UserDetailSerializer
from rest_framework.serializers import ModelSerializer


class FriendListCreateSerializer(ModelSerializer):
    class Meta:
        model = FriendList
        fields = [
            'user',
            'friends',
        ]


class FriendListDetailSerializer(ModelSerializer):
    user = UserListSerializer(read_only=True)
    friends = UserDetailSerializer(many=True, read_only=True)
    class Meta:
        model = FriendList
        fields = [
            'user',
            'friends',
        ]
