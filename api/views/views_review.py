from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models.review import Review
from api.models.titles import Titles
from api.permissions import IsAuthorOrStaff
from api.serializers.serializers_review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    View to CRUD reviews.
    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrStaff]
    serializer_class = ReviewSerializer

    def get_queryset(self, *args, **kwargs):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, id=title_id)
        return Review.objects.filter(title=title)

    def get_serializer_context(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, id=title_id)
        context = super(ReviewViewSet, self).get_serializer_context()
        context.update({'title': title,
                        'author': self.request.user,
                        'request.method': self.request.method})
        return context

    def perform_create(self, serializer, *args, **kwargs):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, id=title_id)
        serializer.save(author=self.request.user, title=title)
