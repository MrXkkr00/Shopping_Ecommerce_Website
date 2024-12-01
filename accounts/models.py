from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField('Phone Number', max_length=20)
    address = models.TextField('Address')
    username = None
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
