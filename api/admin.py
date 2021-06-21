from django.contrib import admin

from api.models.categories import Categories
from api.models.comment import Comment
from api.models.genres import Genres
from api.models.review import Review
from api.models.titles import Titles
from api.models.user import YaUser
from api.registration.forms import YaUserChangeForm, YaUserCreationForm

admin.site.site_header = 'YaMDb API'
EMPTY_VALUE = '-пусто-'


@admin.register(YaUser)
class YaUserAdmin(admin.ModelAdmin):
    """ А representation of a model Group in the admin interface.
    It also defines the following custom values:
    - fields displayed on the change list page of the admin,
    - search box on the admin change list page of the admin,
    - default display value for record’s fields that are empty.
    """
    add_form = YaUserCreationForm
    form = YaUserChangeForm
    list_display = ('username', 'email', 'role',)
    search_fields = ('email',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'text', 'author', 'pub_date',)
    search_fields = ('review', 'text', 'author', 'pub_date',)
    list_filter = ('pub_date'),
    empty_value_display = EMPTY_VALUE


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'score', 'pub_date',)
    search_fields = ('title', 'text', 'author', 'score',)
    list_filter = ('pub_date',)
    empty_value_display = EMPTY_VALUE


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = EMPTY_VALUE
