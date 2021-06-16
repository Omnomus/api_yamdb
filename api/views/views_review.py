from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models.review import Review
from api.models.titles import Titles
# from api.permissions import IsAuthorOrReadOnly
from api.serializers.serializers_review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer

    def get_queryset(self, *args, **kwargs):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, id=title_id)
        return Review.objects.filter(title=title)
