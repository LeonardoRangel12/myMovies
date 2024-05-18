from django import template
from movies.models import Movie, MovieReview

register = template.Library()

@register.filter(name='get_movie_by_id')
def get_movie_by_id_filter(movie_id):
    return Movie.objects.get(id=movie_id)
