from django_filters.rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.filters.filter_titles import TitlesFilter
from api.models.titles import Titles
from api.serializers.serializers_titles import TitlesSerializer
from api.serializers.serializers_titles import TitlesListSerializer


class TitlesViewSet(ModelViewSet):
    queryset = Titles.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TitlesFilter
    # serializer_class = TitlesSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TitlesListSerializer
        return TitlesSerializer
