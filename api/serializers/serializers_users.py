# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models.user import YaUser


class YaUserSerializer(ModelSerializer):

    class Meta:
        model = YaUser
        fields = ['first_name', 'last_name', 'username', 'bio', 'email', 'role']
        lookup_field = 'username'

    # def create(self, validated_data):
    #     user = YaUser.objects.create_user(**validated_data)
    #     return user

    # def validate_email(self, email):
    #     try:
    #         validate_email(email)
    #     except ValidationError:
    #         raise serializers.ValidationError('Given email is invalid')
    #     return email
