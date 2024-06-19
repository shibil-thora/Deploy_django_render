from django.shortcuts import render, HttpResponse, redirect
from .models import Member


def index(request): 
    members = Member.objects.all()
    return render(request, 'index.html', {'members': members}) 

def add_member(request, name): 
    Member.objects.create(name=name) 
    return redirect('index')