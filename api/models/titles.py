from django.db import models

from .genres import Genres
from .categories import Categories
from api.validators.validate_year import validate_year


class Titles(models.Model):
    """Произведения."""
    name = models.CharField('Название', max_length=250, unique=True)
    year = models.PositiveSmallIntegerField(
        'Год создания', null=True, validators=[validate_year])
    description = models.TextField(default='Описание не добавлено')
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория произведения')
    genre = models.ManyToManyField(
        Genres,
        through='TitlesGenres')
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
