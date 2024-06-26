"""
URL configuration for mymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Routers
from movies.views import index, movie, rewiews, handle_login, handle_logout, MoviesByActor, get_credit_name, my_user

# NO DIAGONAL AL FINAL (/ NO)
urlpatterns = [
    path('admin', admin.site.urls),
    path('', index, name="index"),
    path('movie/<int:movie_id>', movie, name="movie"),
    path('movie/<int:movie_id>/reviews', rewiews, name="reviews"),
    path('login', handle_login, name="login"),
    path('movies_by_actor/<int:actor_id>', MoviesByActor, name='movies_by_actor_with_id'),
    path('logout', handle_logout, name="logout"),
    path('get_credit_name/<int:credit_id>', get_credit_name, name='get_credit_name'),
    path('my_user', my_user, name='my_user'),
]

