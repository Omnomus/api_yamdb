from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models.review import Review
from api.models.titles import Titles
# from api.permissions.permission_reviews_comments import IsAuthorOrStaff
from api.serializers.serializers_review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer

    def get_queryset(self, *args, **kwargs):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, id=title_id)
        return Review.objects.filter(title=title)

    def get_serializer_context(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, id=title_id)
        context = super(ReviewViewSet, self).get_serializer_context()
        context.update({'title': title})
        return context
