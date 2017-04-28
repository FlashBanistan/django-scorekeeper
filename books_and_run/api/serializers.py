from rest_framework import serializers
from books_and_run.models import Statistics
from users.api.serializers import UserDetailSerializer



class StatisticsSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(required=False)
    user = UserDetailSerializer()
    class Meta:
        model = Statistics
        fields = [
            # 'pk',
            'user',
            'url',
            'games_won',
            'hands_won',
            'games_played',
            'high_score',
            'low_score',
        ]
