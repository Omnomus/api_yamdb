from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models.titles import Titles
from api.models.user import YaUser


class Review(models.Model):
    """
    Model to represent reviews.
    """
    title = models.ForeignKey(Titles,
                              verbose_name='Произведение',
                              on_delete=models.CASCADE,
                              related_name="reviews")
    text = models.TextField(verbose_name='Текст отзыва')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(YaUser,
                               verbose_name='Автор отзыва',
                               on_delete=models.CASCADE,
                               related_name="reviews")
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=[MinValueValidator(limit_value=1),
                    MaxValueValidator(limit_value=10)]
    )

    class Meta:
        ordering = ("-pub_date",)
        models.UniqueConstraint(
            fields=['author', 'title'],
            name='unique_review'
        )
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return (f'Отзыв {self.post.id} пользователя'
                f'{self.author}, создана {self.pub_date}')
