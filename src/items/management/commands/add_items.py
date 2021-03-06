from django.core.management.base import BaseCommand
from items.models import Item
from django.conf import settings
import requests


URL = "https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json"


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        response = requests.get(url=URL).json()

        for item in response:
            obj, created = Item.objects.update_or_create(
                id=item["id"],
                defaults={
                    "title": item["title"],
                    "description": item["description"],
                    "weight": item["weight_grams"],
                    "price": item["price"],
                },
            )
            if created:
                url = item["image"]
                filename = url.split("/")[-1]
                r = requests.get(url)
                with open(str(settings.MEDIA_ROOT) + "/" + filename, mode="wb") as f:
                    f.write(r.content)
                obj.image = filename
                obj.save()

        return
