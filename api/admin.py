from django.contrib import admin

from api.models.categories import Categories
from api.models.genres import Genres
from api.models.titles import Titles
from api.models.user import YaUser

admin.site.site_header = 'YaMDb API'


@admin.register(YaUser)
class YaUserAdmin(admin.ModelAdmin):
    """ А representation of a model Group in the admin interface.
    It also defines the following custom values:
    - fields displayed on the change list page of the admin,
    - search box on the admin change list page of the admin,
    - default display value for record’s fields that are empty.
    """
    list_display = ('username', 'email', 'role',)
    search_fields = ('username',)
    empty_value_display = '-пусто-'


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'
