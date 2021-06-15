from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models.comment import Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('review',)
        model = Comment
