from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import (
    CharField,
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
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'first_name',
            'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    confirm_email = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'confirm_email',
            'password',
        ]
        # extra_kwargs = {'password': {'write_only': True} }

    def validate_email(self, value):
        data = self.get_initial()
        email1 = value
        confirm_email = data.get('confirm_email')
        if email1 != confirm_email:
            raise ValidationError('Emails must match.')
        user_qs = User.objects.filter(email=confirm_email)
        if user_qs.exists():
            raise ValidationError('This email has already been registered.')

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        confirm_email = value
        if email1 != confirm_email:
            raise ValidationError('Emails must match.')
        return value

    def create(self, validated_data):
        print("In the create")
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        print("VALIDATED DATA: ", validated_data)
        return validated_data



# class UserLoginSerializer(ModelSerializer):
#     token = CharField(allow_blank=True, read_only=True)
#     username = CharField(required=False, allow_blank=True)
#     email = EmailField(label='Email Address', required=False, allow_blank=True)
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password',
#             'token',
#         ]
#         extra_kwargs = {'password': {'write_only': True} }
#
#     def validate(self, data):
#         user_obj = None
#         email = data.get('email', None)
#         username = data.get('username', None)
#         password = data['password']
#         if not email and not username:
#             raise ValidationError('A username or email is required to login.')
#         user = User.objects.filter(
#             Q(email=email) |
#             Q(username=username)
#         ).distinct()
#         user = user.exclude(email__isnull=True).exclude(email__iexact='')
#         if user.exists() and user.count() == 1:
#             user_obj = user.first()
#         else:
#             raise ValidationError('This username/email is not valid.')
#
#         if user_obj:
#             if not user_obj.check_password(password):
#                 raise ValidationError('Incorrect credentials, please try again.')
#         data['token'] = 'SOME RANDOM TOKEN'
#
#         return data
