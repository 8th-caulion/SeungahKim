from django.shortcuts import render, redirect
from .models import Cheer

def home(request) :
    return render(request, 'home.html')

def profile(request) :
    return render(request, 'profile.html')

def future(request) :
    cheers = Cheer.objects.all
    return render(request, 'future.html', {'cheers': cheers})

def create(request) :
    cheer = Cheer()
    cheer.text = request.GET['text']
    cheer.save() #쿼리 메소드
    return redirect('future')