from rest_framework.serializers import ModelSerializer

from api.models.user import YaUser


class YaUserSerializer(ModelSerializer):

    class Meta:
        model = YaUser
        fields = ['first_name', 'last_name', 'username',
                  'bio', 'email', 'role']
        lookup_field = 'username'
