from django.contrib import admin

from api.models.comment import Comment
from api.models.review import Review
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
