from rest_framework import serializers

from api.models.genres import Genres


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('name', 'slug')
