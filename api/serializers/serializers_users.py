from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.authentication.models import YaUser

ROLE_ERROR = {
    'role': 'You can`t change this info'
}
EMAIL_ERROR = {
    'email': 'You can`t change this info'
}


class YaUserSerializer(ModelSerializer):

    class Meta:
        model = YaUser
        fields = ['first_name', 'last_name', 'username',
                  'bio', 'email', 'role']
        lookup_field = 'username'

    def validate(self, data):
        """
        Check that user can`t change it's own role and email.
        """
        user = self.context['request'].user
        if user.role != 'admin':
            if data.get('role'):
                raise serializers.ValidationError(ROLE_ERROR)
            if data.get('email'):
                raise serializers.ValidationError(EMAIL_ERROR)
        return data
