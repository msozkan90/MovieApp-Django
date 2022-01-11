from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name="moviess"
urlpatterns = [
    path('add_rate/', views.addRate, name="add_rate"),
    path('', views.index,name="index"),
    path('movies', views.movies,name="movies"),
    path('actors/', views.actors,name="actors"),
    path('actors/<slug:slug>/', views.actor_detail,name="actors_detail"),
    path('<slug:slug>/', views.movie_detail,name="movies_detail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)