from django.db import models

from api.models import genres, titles


class TitlesGenres(models.Model):
    """
    Auxiliary model for relationship Titles-Genres (many-to-many).
    """
    titles = models.ForeignKey(titles.Titles, on_delete=models.CASCADE)
    genres = models.ForeignKey(genres.Genres, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['titles', 'genres'],
                name='unique_genre')]

    def __str__(self):
        return f'{self.titles}{self.genres}'
