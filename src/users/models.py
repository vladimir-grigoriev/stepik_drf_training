from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(verbose_name="Отчество", max_length=100)
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    adress = models.CharField(verbose_name="Адрес", max_length=50)

    def __str__(self):
        return f"Пользователь №{self.pk}"
