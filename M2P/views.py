from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from M2P.models import Sport


def index(request):
    return render(request, 'index.html')


def esports(request):
    sport_list = Sport.objects.order_by('sportName')[:5]
    context = {'sport_list': sport_list}
    return render(request, 'esports.html', context)


def localitzacio(request):
    return render(request, 'localitzacio.html')


def event(request):
    return render(request, 'events.html')

def amics(request):
    return render(request, 'amics.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
