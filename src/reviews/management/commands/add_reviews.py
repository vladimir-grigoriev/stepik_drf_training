from django.core.management.base import BaseCommand
from reviews.models import Review
from users.models import User
import requests
import datetime


URL = (
    "https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json"
)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        response = requests.get(url=URL).json()
        for review in response:
            rev_created = datetime.datetime.strptime(review["created_at"], "%Y-%m-%d")
            if review["published_at"]:
                rev_published = datetime.datetime.strptime(
                    review["published_at"], "%Y-%m-%d"
                )
            else:
                rev_published = "2021-01-01"

            obj, created = Review.objects.get_or_create(
                id=review["id"],
                defaults={
                    "author": User.objects.get(id=review["author"]),
                    "text": review["content"],
                    "created_at": rev_created if rev_created != "" else "2021-01-01",
                    "published_at": rev_published
                    if rev_published != ""
                    else "2021-01-01",
                    "status": review["status"],
                },
            )
        return
