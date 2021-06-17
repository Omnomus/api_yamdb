# import datetime

# import jwt
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models.user import YaUser

# class RegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField(write_only=True)

#     class Meta:
#         models = YaUser
#         fields = ['email']

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         if not email():
#             raise ValueError('Введите адрес электронной почты!')
#         return attrs

#     def create(self, validated_data):


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = YaUser
        fields = ('id', YaUser.USERNAME_FIELD, "password", 'full_name',
                  'is_active', 'links', )
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        if 'email' not in validated_data:
            raise ValueError('Email is required!')
        user = get_user_model().objects.create(
            email=validated_data['email']
        )
        user.is_active = False
        user.save()
        confirmation_code = get_random_string(length=11)
        # confirmation_code = jwt.encode({
        #     'id': user.id,
        #     'exp': datetime.timedelta(hours=1)
        # }, settings.SECRET_KEY, algorithm='HS256')
        send_mail(
            'Your confirmation code is here!',
            confirmation_code,
            'YaMDb@yamdb.com',
            validated_data['email']
        )
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['confirmation_code'] = serializers.CharField(required=True)
        self.fields.pop('password')

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # if settings.UPDATE_LAST_LOGIN:
        #     update_last_login(None, self.user)

        return data
