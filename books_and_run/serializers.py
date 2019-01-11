from rest_framework import serializers
from books_and_run.models import Statistics
from users.serializers import UserSerializer



class StatisticsSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(required=False)
    user = UserSerializer()
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
