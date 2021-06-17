from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    def validate(self, data):
        review = Review.objects.filter(title=self.context['title'],
                                       author=self.context['author'])
        if review.exists():
            raise serializers.ValidationError(
                'Вы уже писали отзыв на это произведение.'
            )
        return data

    class Meta:
        fields = '__all__'
        read_only_fields = ('title',)
        model = Review
