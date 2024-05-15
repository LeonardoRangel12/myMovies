from django.shortcuts import render
from django.urls import resolve
from movies.models import Movie, MovieReview
from django.http import HttpResponse
from .forms import ReviewsForm
# Create your views here.

# Index
def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})

# To see movies
def movie(request, movie_id):
    
    movie = Movie.objects.get(id=movie_id)
    
    return render(request, "movie.html", {"movie": movie})

def rewiews(request, movie_id):
    if request.method == "GET":
        reviews = MovieReview.objects.filter(movie=movie_id)
        
        response = HttpResponse(reviews)
        response.status_code = 200
        return response
    
    if request.method == "POST":
        
        form = ReviewsForm(request.POST)
        form.movie_id = movie_id
        
        if Movie.objects.filter(id=movie_id).exists() == False:
            response = HttpResponse("Movie does not exist")
            response.status_code = 404
            
            return response
        
        if form.is_valid():
            movie_review = form.save(commit=False)
            movie_review.save()
            
            response = HttpResponse("Review created")
            response.status_code = 201
            
            return response
        
        else:
            response = HttpResponse("Error with form")
            response.status_code = 400
            
            return response
    else:
        response = HttpResponse("Method not allowed")
        response.status_code = 405
        
        return response


# def get_name(request):
#     if request.method == "POST":
#         form = NameForm(request.POST)
        
#         if form.is_valid():
#             print(form.cleaned_data)
            
#             return render(request, "movies/name_ok.html", {"form": form})
#     else:
#         form = NameForm()
        
#     return render(request, "movies/name.html", {"form" : form})