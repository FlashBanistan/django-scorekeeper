from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

User = get_user_model()

"""
Account serializers
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True} }

    # def validate(self, data):
    #     email = data['email']
    #     user_qs = User.objects.filter(email=email)
    #     if user_qs.exists():
    #         raise ValidationError('This user has already registered.')
    #     return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = value
        email2 = data.get('email2')
        if email1 != email2:
            raise ValidationError('Emails must match.')
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError('This email has already been registered.')

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('Emails must match.')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
