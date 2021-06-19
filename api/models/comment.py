from django.db import models

from api.authentication.models import YaUser
from api.models.review import Review


class Comment(models.Model):
    """
    Model to represent comments.
    """
    review = models.ForeignKey(Review,
                               verbose_name='Отзыв',
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(YaUser,
                               on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (f"Коментарий пользователя {self.author} к отзыву"
                f"{self.review.id}, создана {self.pub_date}")
