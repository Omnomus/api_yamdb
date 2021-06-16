from rest_framework import serializers

from api.models.categories import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name', 'slug')
        lookup_field = 'slug'
