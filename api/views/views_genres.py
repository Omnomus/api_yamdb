from django_filters.rest_framework import filters
from rest_framework import filters, mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from api.models.genres import Genres
from api.serializers.serializers_genres import GenresSerializer


class ListCreateDestroyViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               GenericViewSet):
    pass


class GenresViewSet(ListCreateDestroyViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
