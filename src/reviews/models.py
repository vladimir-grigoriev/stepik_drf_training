from django.db import models
from users.models import User


class Review(models.Model):
    class ReviewStatus(models.TextChoices):
        NEW = "new", ("Moderation")
        PUBLISHED = "published", ("Published")
        HIDDEN = "hidden", ("Denied")

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    text = models.TextField(verbose_name="Текст отзыва", blank=False, null=False)

    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    published_at = models.DateTimeField(verbose_name="Дата публикации", auto_now=True)

    status = models.CharField(
        verbose_name="Статус",
        max_length=9,
        choices=ReviewStatus.choices,
        default=ReviewStatus.NEW,
    )
