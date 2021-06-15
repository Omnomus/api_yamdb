from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from api.views.views_categories import CategoriesViewSet
from api.views.views_genres import GenresViewSet
from api.views.views_titles import TitlesViewSet

router_v1 = DefaultRouter()

router_v1.register('v1/categories', CategoriesViewSet, basename='categories')
router_v1.register('v1/genres', GenresViewSet, basename='genres')
router_v1.register('v1/titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('', include(router_v1.urls)),
]
