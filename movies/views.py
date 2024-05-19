from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from movies.models import Movie, MovieReview
from django.http import HttpResponse
from .forms import ReviewsForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json
# Create your views here.

# COOKIES THEY ARE GOING TO BE JSONS I DONT CARE
# kys
# "movies_history"

def appendMovieToHistory(currentHistoryStr, movieId):
    historyArr = json.loads(currentHistoryStr)
    if movieId not in historyArr:
        historyArr.append(movieId)
    return json.dumps(historyArr)

# Index
def index(request):
    movies = Movie.objects.all()
    response = HttpResponse(render(request, "index.html", {"movies": movies, "movies_history": ["a"]}))
    if not 'movies_history' in request.COOKIES:
        response.set_cookie('movies_history', '[]')
    else:
        seen_movies_ids = json.loads(request.COOKIES['movies_history'])
        response = HttpResponse(render(request, "index.html", {"movies": movies, "movies_history": seen_movies_ids}))
        
    return response

# To see movies
def movie(request, movie_id):
    currentHistoryStr = "[]"
    if 'movies_history' in request.COOKIES:
        currentHistoryStr =  request.COOKIES['movies_history']
    movie = Movie.objects.get(id=movie_id)
    reviews = MovieReview.objects.filter(movie=movie_id)
    response = render(request, "movie.html", {"movie": movie, "reviews": reviews})
    new_history_value = appendMovieToHistory(currentHistoryStr,movie_id)
    response.set_cookie("movies_history", new_history_value)
    return response

def rewiews(request, movie_id):
    # if request.method == "GET":
    #     reviews = MovieReview.objects.filter(movie=movie_id)
        
    #     response = HttpResponse(reviews)
    #     response.status_code = 200
    #     return response
    
    @login_required
    def post_review(request, movie_id):
        
        form = ReviewsForm(request.POST)
            
        movie = get_object_or_404(Movie, id=movie_id)
        
        if form.is_valid():
            review = MovieReview(
                user=request.user,
                movie=movie,
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
    
    
# Remove auth   
def handle_logout(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")
    
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