from django.contrib.auth.models import AbstractUser, BaseUserManager
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
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of username.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a YaUser with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address!')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with the given email and password.
        """
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.has_module_permission = True
        user.role = 'admin'
        user.save()
        return user


class YaUser(AbstractUser):
    """ Defines YaUser model and its database fields."""
    username = models.CharField(
        'Username', max_length=255, blank=True, null=True, unique=True
    )
    bio = models.TextField('About myself', max_length=1000, blank=True)
    email = models.EmailField(
        'Email', max_length=255, unique=True
    )
    role = models.CharField(
        max_length=20, choices=USER_ROLE_CHOICES, default='user'
    )
    password = models.CharField(max_length=128, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = YaUserManager()

    class Meta:
        ordering = ('email',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.email)
