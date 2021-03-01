from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class Review(models.Model):

    class ReviewStatus(models.TextChoices):
        ON_MODERATION = 'MOD', _('На модерации')
        PUBLISHED = 'PUB', _('Опубликовано')
        DENIED = 'DEN', _('Отклонено')
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    text = models.TextField(
        verbose_name='Текст отзыва',
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        auto_now=False
    )

    published_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now=True,
        auto_now_add=False
    )

    status = models.CharField(
        verbose_name='Статус',
        max_length=3,
        choices=ReviewStatus.choices,
        default=ReviewStatus.ON_MODERATION
    )
