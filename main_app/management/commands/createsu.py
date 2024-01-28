from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(email='postgres@gmail.com').exists():
            User.objects.create_superuser(
                email=os.environ.get("SUPERUSER_EMAIL"),
                password=os.environ.get("SUPERUSER_PASSWORD")
            )
            print('Superuser has been created.')
        else:
            print('Superuser already exists.')
