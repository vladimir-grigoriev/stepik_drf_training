from django.db import models


class Item(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)

    description = models.TextField(
        verbose_name="Описание",
    )

    image = models.ImageField(
        verbose_name="Картинка",
        upload_to="items/"
    )

    weight = models.PositiveSmallIntegerField(verbose_name="Вес в граммах")

    price = models.DecimalField(
        verbose_name="Цена в рублях", max_digits=19, decimal_places=2
    )

    def __str___(self):
        return f'Набор №{self.id} "{self.title}"'
