from django.contrib import admin

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
