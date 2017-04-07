from rest_framework import serializers
from books_and_run.models import Statistics



class StatisticsSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(required=False)
    class Meta:
        model = Statistics
        fields = [
            'url',
            # 'user',
            # 'pk',
            'games_won',
            'hands_won',
            'games_played',
            'high_score',
            'low_score',
        ]
