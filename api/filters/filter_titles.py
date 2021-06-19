import django_filters

from api.models.titles import Titles


class TitlesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains')
    year = django_filters.NumberFilter(
        field_name='year', lookup_expr='iexact')
    genre = django_filters.CharFilter(
        field_name='genre__slug', lookup_expr='iexact')
    category = django_filters.CharFilter(
        field_name='category__slug', lookup_expr='iexact')

    class Meta:
        model = Titles
        fields = ('name', 'year', 'genre', 'category')
