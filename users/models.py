from django.contrib.auth.models import AbstractUser
from django.db import models


NULLEBELL = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Указите почту"
    )
    phone = models.CharField(max_length=45, **NULLEBELL, verbose_name="Телефон")
    city = models.CharField(max_length=60, verbose_name="Город", **NULLEBELL)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", **NULLEBELL
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
