from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name="account"
urlpatterns = [
    path('login', views.sign_in,name="sign_in"),
    path('register', views.register,name="register"),
    path('logout/', views.sign_out,name="sign_out"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)