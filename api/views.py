from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Comment, Review, Title, User
# from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, ReviewSerializer

User = get_user_model()


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer

    def get_queryset(self, *args, **kwargs):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return Review.objects.filter(title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return Comment.objects.filter(review=review)

    def perform_create(self, serializer, *args, **kwargs):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)
