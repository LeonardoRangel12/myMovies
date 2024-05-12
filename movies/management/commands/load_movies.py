from django.core.management.base import BaseCommand, CommandError
from movies.models import Genre, Movie, Person, Job, MovieCredit

from django.utils.timezone import timezone
from datetime import datetime

class Command(BaseCommand):
    help = "Loads a movie, we assume the database is empty"

    def handle(self, *args, **options):
        print("Jala")
        jobs = ['Director', 'Producer', 'Actor', 'Voice Actor']
        genres = ['Action', 'Adventure', 'Animation', 'Drama', 'Science Fiction', 'Thriller']

        for name in genres:
            g = Genre(name=name)
            g.save()

        for job in jobs:
            j = Job(name=job)
            j.save()

        m1 = Movie(title='The Shawshank Redemption',
                   overview='Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.',
                   release_date=datetime(94, 9, 23, tzinfo=timezone.utc),
                   running_time=142,
                   budget=25000000,
                   tmdb_id=278,
                   revenue=28341469,
                   poster_path='')
        m1.save()
        print("Guarda movie")
        j = Job.objects.get(name='Actor')

        for name in ['John David Washington',
                     'Madeleine Yuna Voyles',
                     'Gemma Chan']:
            a = Person.objects.create(name=name)
            MovieCredit.objects.create(person=a, movie=m1, job=j)