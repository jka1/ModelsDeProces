from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def esports(request):
    return render(request, 'esports.html')


def pista(request):
    return render(request, 'pista.html')


def event(request):
    return render(request, 'events.html')
