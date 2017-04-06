from rest_framework import serializers
from books_and_run.models import Statistics
from accounts.api.serializers import UserDetailSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


from django.core.exceptions import ObjectDoesNotExist

"""
Statistics endpoints
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# class StatisticsCreateSerializer(ModelSerializer):
#     class Meta:
#         model = Statistics
#         fields = [
#             'user',
#             'games_won',
#             'hands_won',
#             'games_played',
#             'high_score',
#             'low_score',
#         ]
#
#
# class StatisticsDetailSerializer(ModelSerializer):
#     user = UserDetailSerializer(read_only=True)
#     class Meta:
#         model = Statistics
#         fields = [
#             'user',
#             'games_won',
#             'hands_won',
#             'games_played',
#             'high_score',
#             'low_score',
#         ]
#
# class StatisticsUpdateSerializer(ModelSerializer):
#     class Meta:
#         model = Statistics
#         fields = [
#             'games_won',
#             'hands_won',
#             'games_played',
#             'high_score',
#             'low_score',
#         ]


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
