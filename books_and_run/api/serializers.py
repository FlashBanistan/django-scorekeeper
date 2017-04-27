from rest_framework import serializers
from books_and_run.models import Statistics
from users.api.serializers import UserListSerializer



class StatisticsSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(required=False)
    user = UserListSerializer()
    class Meta:
        model = Statistics
        fields = [
            'url',
            'user',
            # 'pk',
            'games_won',
            'hands_won',
            'games_played',
            'high_score',
            'low_score',
        ]
