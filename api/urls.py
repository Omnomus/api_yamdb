from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.views_categories import CategoriesViewSet
from api.views.views_comment import CommentViewSet
from api.views.views_genres import GenresViewSet
from api.views.views_review import ReviewViewSet
from api.views.views_titles import TitlesViewSet

router_v1 = DefaultRouter()

router_v1.register('v1/categories', CategoriesViewSet, basename='categories')
router_v1.register('v1/genres', GenresViewSet, basename='genres')
router_v1.register('v1/titles', TitlesViewSet, basename='titles')
router_v1.register(
    r'v1/titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('', include(router_v1.urls)),
]
