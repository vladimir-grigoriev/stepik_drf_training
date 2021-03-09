from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Логин", unique=True, max_length=150, blank=True, null=True
    )
    middle_name = models.CharField(
        verbose_name="Отчество", max_length=100, blank=True, null=True
    )
    phone = models.CharField(
        verbose_name="Телефон", max_length=20, blank=True, null=True
    )
    adress = models.CharField(verbose_name="Адрес", max_length=50)

    def set_username(self):
        self.username = self.email[: self.email.find("@")]

    def __str__(self):
        return f"User №{self.pk}"
