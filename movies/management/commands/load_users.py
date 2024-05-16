from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
class Command(BaseCommand):
    
    def handle(self, *args, **options):
        user = User.objects.create_user(username='nanimon384', password='nanimon384')