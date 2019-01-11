from django.contrib.auth import get_user_model
from rest_framework.serializers import EmailField, HyperlinkedModelSerializer, ModelSerializer, ValidationError

User = get_user_model()



class UserDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'pk'
        ]


class UserListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
        ]


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    def validate_username(self, value):
        raise ValidationError('You cannot change your username. Please contact an administrator.')


class UserCreateSerializer(ModelSerializer):
    confirm_email = EmailField(write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'password',
        ]

        """
        Fields added to 'extra_kwargs' with 'write_only': 'True' will not be returned in the response:
        """
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, data):
        print("Validating...")
        """
        Check that the emails match:
        """
        if data['email'] != data['confirm_email']:
            raise ValidationError("Emails do not match.")
        """
        Check if the user already exists:
        """
        user = User.objects.filter(email=data['email'])
        if user.exists():
            raise ValidationError('This email has already been registered.')

        return data


    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
