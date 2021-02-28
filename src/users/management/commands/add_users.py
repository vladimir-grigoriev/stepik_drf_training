from django.core.management.base import BaseCommand
from users.models import User
import requests


URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        response = requests.get(url=URL).json()
        for user in response:
            obj, created = User.objects.get_or_create(
                id=user['id']+1,
                defaults={
                    'email': user['email'],
                    'username': user['email'].split('@')[0],
                    'first_name': user['info']['name'],
                    'last_name': user['info']['surname'],
                    'middle_name': user['info']['patronymic'],
                    'phone': user['contacts']['phoneNumber'],
                    'adress': user['city_kladr']
                }
            )
            if created:
                obj.set_password(user['password'])
                obj.save()
        return