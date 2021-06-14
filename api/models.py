from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Title(models.Model):
    pass


class Review(models.Model):
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name="reviews")
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
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


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField(auto_now_add=True)
