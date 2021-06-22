from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from api.models.user import YaUser
from api.authentication.forms import YaUserChangeForm, YaUserCreationForm

admin.site.site_header = 'YaMDb API'


@admin.register(YaUser)
class YaUserAdmin(admin.ModelAdmin):
    add_form = YaUserCreationForm
    form = YaUserChangeForm
    list_display = ('username', 'email', 'role',)
    search_fields = ('email',)


models = apps.get_app_config('api').get_models()
for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
