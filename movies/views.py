from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from movies.models import Movie, MovieReview
from django.http import HttpResponse
from .forms import ReviewsForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

# Index
def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})

# To see movies
def movie(request, movie_id):
    
    movie = Movie.objects.get(id=movie_id)
    reviews = MovieReview.objects.filter(movie=movie_id)
    return render(request, "movie.html", {"movie": movie, "reviews": reviews})

def rewiews(request, movie_id):
    # if request.method == "GET":
    #     reviews = MovieReview.objects.filter(movie=movie_id)
        
    #     response = HttpResponse(reviews)
    #     response.status_code = 200
    #     return response
    
    @login_required
    def post_review(request, movie_id):
        
        form = ReviewsForm(request.POST)
            
        if Movie.objects.filter(id=movie_id).exists() == False:
            response = HttpResponse("Movie does not exist")
            response.status_code = 404
            
            return response
        
        if form.is_valid():
            review = MovieReview(
                user=1,
                movie=movie_id,
                rating=form.cleaned_data["rating"],
                review=form.cleaned_data["review"]
            )
            
            review.save()
            
            response = HttpResponse("Review created")
            response.status_code = 201
            
            return response
        
        else:
            response = HttpResponse("Error with form")
            response.status_code = 400
            
            return response
    if request.method == "POST":
        return post_review(request, movie_id)
        
    else:
        response = HttpResponse("Method not allowed")
        response.status_code = 405
        
        return response
    
       


def handle_login (request):
    if request.method == "GET":
        return render(request, "login.html")
    
    # Logins
    if request.method == "POST":
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            # print(form.cleaned_data)
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("/")
                
            else:
                response = HttpResponse("User not found")
                response.status_code = 404
                
                return response
        
        else:
            response = HttpResponse("Error with form")
            response.status_code = 400
            
            return response


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