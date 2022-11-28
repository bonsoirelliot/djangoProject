from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    username = models.CharField('Имя пользователя', max_length=50)
    first_name = models.CharField('Полное имя', max_length=100)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
