# from django.contrib.auth import get_user_model
# from rest_framework import viewsets
#
# from .serializers import UserDetailSerializer
# from scorekeeper.mixins import DefaultsMixin
#
# User = get_user_model()
#
#
#
# class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer




"""
Everything under here is in testing:
"""
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserCreateSerializer, UserDetailSerializer
from scorekeeper.mixins import DefaultsMixin

User = get_user_model()

class CustomUserViewSet(DefaultsMixin, viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serialized_users = UserDetailSerializer(users, context={'request': request}, many=True).data

        return Response(serialized_users)


    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            new_user = User(username=serializer.data.get('username'), email=serializer.data.get('email'))
            new_user.set_password(serializer.data.get('password'))
            new_user.save()
            serialized_user = UserDetailSerializer(new_user, context={'request': request}).data
            return Response(serialized_user)

        return Response("Couldn't process request")


    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserDetailSerializer(user)

        return Response(serializer.data)


    def update(self, request):
        pass


    def partial_update(self, request, pk=None):
        pass


    def destroy(self, request, pk=None):
        pass
