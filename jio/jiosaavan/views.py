from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,"home.html")

def jiomusic(request):
    return render(request,"jiomusic.html")

def contactus(request):
    return render(request, "Contact.html")

def register(request):
    if request.method== "POST":
        Name= request.POST.get('usname')
        Email= request.POST.get('email')
        Password= request.POST.get('password')
        new_user = User.objects.create_user(Name,Email,Password)
        new_user.save()
    return render(request, "Contact.html")
