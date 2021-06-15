import django_filters
from django.db.models.functions import Lower

from api.models.titles import Titles


class TitlesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='name_filter')
    year = django_filters.NumberFilter(field_name='year', lookup_expr='iexact')
    genre = django_filters.CharFilter(
        field_name='genre__slug', lookup_expr='iexact')
    category = django_filters.CharFilter(
        field_name='category__slug', lookup_expr='iexact')

    class Meta:
        model = Titles
        fields = '__all__'

    def name_filter(self, queryset, name, value):
        lower_name_titles = Titles.objects.annotate(lower_name=Lower(name))
        # не работает с кириллицей
        # queryset = Titles.objects.filter(Lower(name)__icontains=value)
        queryset = lower_name_titles.filter(lower_name__contains=value)
        return queryset
