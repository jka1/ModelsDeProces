from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def esports(request):
    return HttpResponse("Aixo serà la pàgina dels esports.")


def pista(request):
    response = "Aixo serà la pàgina de una pista"
    return HttpResponse(response)


def event(request):
    return HttpResponse("Això sera la pagina de un event.")
