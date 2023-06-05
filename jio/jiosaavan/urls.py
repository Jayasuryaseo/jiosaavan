from django.contrib import admin
from django.urls import path
from .views import  home, jiomusic, contactus

urlpatterns = [
    
    path('', home),
    path('jiomusic/', jiomusic),
    path('Contact/', contactus),
]