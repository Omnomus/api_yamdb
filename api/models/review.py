from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models.titles import Titles
from api.models.user import YaUser


class Review(models.Model):
    title = models.ForeignKey(Titles,
                              on_delete=models.CASCADE,
                              related_name="reviews")
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(YaUser,
                               on_delete=models.CASCADE,
                               related_name="reviews")
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(limit_value=1),
                    MaxValueValidator(limit_value=10)]
    )

    class Meta:
        ordering = ("-pub_date",)
        models.UniqueConstraint(
            fields=['author', 'title'],
            name='unique_review'
        )

    def __str__(self):
        return (f'Отзыв {self.post.id} пользователя'
                f'{self.author}, создана {self.pub_date}')
