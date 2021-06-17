from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from api.filters.filter_titles import TitlesFilter
from api.models.titles import Titles
from api.permissions.permissions_titles import IsAdminOrReadOnly
from api.serializers.serializers_titles import TitlesSerializer
from api.serializers.serializers_titles import TitlesListSerializer


class TitlesViewSet(ModelViewSet):
    queryset = Titles.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TitlesListSerializer
        return TitlesSerializer
