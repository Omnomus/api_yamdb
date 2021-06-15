from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.review import Review
from ..models.title import Title
# from ..permissions import IsAuthorOrReadOnly
from ..serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer

    def get_queryset(self, *args, **kwargs):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return Review.objects.filter(title=title)
