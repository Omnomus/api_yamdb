from django.db import models

from .titles import Titles
from .genres import Genres


class TitlesGenres(models.Model):
    titles = models.ForeignKey(Titles, on_delete=models.CASCADE)
    genres = models.ForeignKey(Genres, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['titles', 'genres'],
                name='unique_genre')]

    def __str__(self):
        return f'{self.titles}{self.genres}'
