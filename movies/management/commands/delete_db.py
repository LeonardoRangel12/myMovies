from django.core.management.base import BaseCommand, CommandError
from movies.models import Genre, Movie, Person, Job, MovieCredit, MovieReview

from django.utils.timezone import timezone
from datetime import datetime
import requests
import random
import json
class Command(BaseCommand):
    help = "Deletes all data from the database"
    def handle(self, *args, **options):
        
        # Remove all data from db
        Genre.objects.all().delete()
        Job.objects.all().delete()
        Person.objects.all().delete()
        Movie.objects.all().delete()
        MovieCredit.objects.all().delete()
        MovieReview.objects.all().delete()
        