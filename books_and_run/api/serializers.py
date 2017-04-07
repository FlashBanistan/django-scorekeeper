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

    # def update(self, instance, validated_data):
    #     instance.is_winner = ""
    #     print("1")
    #     return instance



class StatisticsUpdateSerializer(serializers.Serializer):
    is_winner = serializers.BooleanField()
    num_hands_won = serializers.IntegerField()
    score = serializers.IntegerField()

    class Meta:
        fields = [
            'is_winner',
            'num_hands_won',
            'score',
        ]
