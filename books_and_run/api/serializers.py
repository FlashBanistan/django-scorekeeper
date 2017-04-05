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
    # user = UserDetailSerializer(read_only=True)
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

    # def create(self, validated_data):
    #     # Check if user exists
    #     user = None
    #
    #     # print('User: ', user)
    #     # print("")
    #     # print("dir Self: ")
    #     # print(dir(self))
    #     # print("")
    #     #
    #     # print("validated Data: ")
    #     # print(validated_data)
    #     # print("")
    #
    #     return Statistics(**validated_data)

    # def validate(self, data):
    #     print("")
    #     print("dir(data): ", dir(data))
    #     print("")
    #
    #     print("data.values", data.values)
    #     print("")
    #
    #     print("dir(self): ", dir(self))
    #     print("")
    #
    #     print("self.initital_data: ", self.initial_data)
    #     print("")
    #
    #     return data
