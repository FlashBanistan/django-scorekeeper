from django.contrib.auth import get_user_model
from rest_framework.serializers import EmailField, HyperlinkedModelSerializer, ModelSerializer, ValidationError

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'friend_set',
            'friendship_creator_set',
            # 'date_joined',
            'password',
        ]

        """
        Fields added to 'extra_kwargs' with 'write_only': 'True' will not be returned in the response:
        """
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': False,
                'style': {"input_type": "password"}
            },
            'first_name': {
                'required': True,
            }
        }

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
