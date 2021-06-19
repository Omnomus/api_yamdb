from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from api.authentication.models import YaUser


class YaUserCreationForm(UserCreationForm):

    class Meta:
        model = YaUser
        fields = ('email',)


class YaUserChangeForm(UserChangeForm):

    class Meta:
        model = YaUser
        fields = ('email',)
