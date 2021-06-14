from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager)
from django.db import models

ROLE_USER = 'user'
ROLE_MODERATOR = 'moderator'
ROLE_ADMIN = 'admin'
USER_ROLE_CHOICES = (
    (ROLE_USER, 'user'),
    (ROLE_MODERATOR, 'moderator'),
    (ROLE_ADMIN, 'admin'),
)


class YaUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given
        username, email and password.
        """
        if not username:
            raise ValueError('Users must have a username!')
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given
        username, email and rassword.
        """
        user = self.create_user(
            username,
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class YaUser(AbstractBaseUser):
    """ Defines User model and its database fields."""
    first_name = models.CharField('Имя', max_length=255, blank=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True)
    username = models.CharField('Username', max_length=255, unique=True)
    bio = models.TextField('О себе', max_length=1000, blank=True)
    email = models.EmailField(
        'Адрес электронной почты', max_length=255, unique=True
    )
    role = models.CharField(
        max_length=20, choices=USER_ROLE_CHOICES, default='user'
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = YaUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
