from rest_framework import serializers
from friendship.models import FriendshipRequest

class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = [
            'from_user',
            'to_user',
            'date_created',
        ]