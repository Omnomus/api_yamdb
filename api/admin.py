from django.contrib import admin

from api.authentication.forms import YaUserChangeForm, YaUserCreationForm
from api.authentication.models import YaUser
from api.models.categories import Categories
from api.models.comment import Comment
from api.models.genres import Genres
from api.models.review import Review
from api.models.titles import Titles

admin.site.site_header = 'YaMDb API'


@admin.register(YaUser)
class YaUserAdmin(admin.ModelAdmin):
    add_form = YaUserCreationForm
    form = YaUserChangeForm
    list_display = ('username', 'email', 'role',)
    search_fields = ('email',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'text', 'author', 'pub_date',)
    search_fields = ('review', 'text', 'author', 'pub_date',)
    list_filter = ('pub_date'),
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'score', 'pub_date',)
    search_fields = ('title', 'text', 'author', 'score',)
    list_filter = ('pub_date',)
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
