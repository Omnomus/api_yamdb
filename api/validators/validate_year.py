from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    if value > datetime.now().year:
        raise ValidationError(
            'Это произведение еще не опубликовано! Проверьте год издания.')
