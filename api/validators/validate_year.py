from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    """
    Validate year in Titles model.
    Year should not be earlier than the current.
    """
    if value > datetime.now().year:
        raise ValidationError(
            'Can not post future titles - year is in future')
