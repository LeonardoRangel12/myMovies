from django.shortcuts import render
from django.urls import resolve
from movies.models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})

def movie(request, movie_id):
    
    movie = Movie.objects.get(id=movie_id)
    
    return render(request, "movie.html", {"movie": movie})


# def get_name(request):
#     if request.method == "POST":
#         form = NameForm(request.POST)
        
#         if form.is_valid():
#             print(form.cleaned_data)
            
#             return render(request, "movies/name_ok.html", {"form": form})
#     else:
#         form = NameForm()
        
#     return render(request, "movies/name.html", {"form" : form})