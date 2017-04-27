from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer, UserUpdateSerializer
from scorekeeper.mixins import DefaultsMixin

User = get_user_model()

class UserViewSet(DefaultsMixin, viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serialized_users = UserListSerializer(users, context={'request': request}, many=True).data

        return Response(serialized_users)


    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            """
            Calling serializer.save() will go into the create method on the serializer:
            """
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserDetailSerializer(user, context={'request': request})

        return Response(serializer.data)


    def update(self, request, pk=None):
        queryset = User.objects.all()
        instance = queryset.get(pk=pk)
        serializer = UserUpdateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


    def partial_update(self, request, pk=None):
        pass


    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()

        return Response(status=201)
