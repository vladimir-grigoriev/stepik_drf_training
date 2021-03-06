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
            a = review["published_at"].split("-")
            print(a)
            obj, created = Review.objects.get_or_create(
                id=review["id"],
                defaults={
                    "author": User.objects.get(id=review["author"]),
                    "text": review["content"],
                    "created_at": datetime.datetime(
                        year=int(review["created_at"].split("-")[0]),
                        month=int(review["created_at"].split("-")[1]),
                        day=int(review["created_at"].split("-")[2]),
                        hour=0,
                        minute=0,
                        second=0,
                        microsecond=0,
                    ),
                    "published_at": datetime.datetime(
                        year=int(review["published_at"].split("-")[0]),
                        month=int(review["published_at"].split("-")[1]),
                        day=int(review["published_at"].split("-")[2]),
                        hour=0,
                        minute=0,
                        second=0,
                        microsecond=0,
                    ),
                    "status": review["status"][:3].upper(),
                },
            )

        return
