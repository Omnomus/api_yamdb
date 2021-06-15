from django.core.exceptions import ValidationError
from datetime import datetime


def validate_year(value):
    if value > datetime.now().year:
        raise ValidationError(
            'Это произведение еще не опубликовано! Проверьте год издания.')
