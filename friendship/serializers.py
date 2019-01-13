from rest_framework import serializers
from friendship.models import FriendRequest, Friend

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = [
            'url',
            'from_user',
            'to_user',
            'date_created',
        ]
        extra_kwargs = {
            'from_user': {
                'read_only': True,
            },
        }

    def create(self, validated_data):
        req_user = self.context['request'].user
        to_user = validated_data.get('to_user')
        return FriendRequest.objects.send_friend_request(from_user=req_user, to_user=to_user)


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = [
            'url',
            'to_user',
            'from_user',
            'created', 
        ]
