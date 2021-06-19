from django_filters.rest_framework import filters
from rest_framework import filters, mixins
from rest_framework.viewsets import GenericViewSet

from api.models.categories import Categories
from api.permissions import IsAdminOrReadOnly
from api.serializers.serializers_categories import CategoriesSerializer


class ListCreateDestroyViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               GenericViewSet):
    pass


class CategoriesViewSet(ListCreateDestroyViewSet):
    """
    View to create, list and destroy categories.

    * List method is available for Anonymous,
    others - for authenticated admin only.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
