from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models.review import Review
from api.models.user import YaUser


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=YaUser.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('title',)
        model = Review
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['author', 'title'],
                message='Вы уже писали отзыв на это произведение.'
            )
        ]
