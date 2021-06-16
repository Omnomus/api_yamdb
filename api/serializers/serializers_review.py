from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    title = serializers.SerializerMethodField()

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

    def get_title(self):
        return self.context['title']
