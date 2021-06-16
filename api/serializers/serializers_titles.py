from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models.categories import Categories
from api.models.genres import Genres
from api.models.titles import Titles
from api.models.titlesgenres import TitlesGenres
from api.serializers.serializers_categories import CategoriesSerializer
from api.serializers.serializers_genres import GenresSerializer


class TitlesSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True,
        required=False)
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Categories.objects.all(), required=False)

    class Meta:
        model = Titles
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category')

    def create(self, validated_data):
        if 'genre' not in self.initial_data:
            title = Titles.objects.create(**validated_data)
        else:
            slugs = validated_data.pop('genre')
            title = Titles.objects.create(**validated_data)
            for slug in slugs:
                try:
                    genre = Genres.objects.get(name=slug)
                except Exception:
                    pass
                else:
                    TitlesGenres.objects.create(genres=genre, titles=title)
        return title

    def update(self, title, validated_data):
        if 'genre' in self.initial_data:
            slugs = validated_data.pop('genre')
            for slug in slugs:
                try:
                    genre = Genres.objects.get(name=slug)
                except Exception:
                    raise ValidationError(
                        f'Указан несуществующий жанр - {slug}')
                else:
                    TitlesGenres.objects.get_or_create(
                        genres=genre, titles=title)
        title = super().update(title, validated_data)
        return title


class TitlesListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer()

    class Meta:
        model = Titles
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category')

    def get_rating(self, title):
        # return title.reviews.aggregate(Avg(score))
        pass
