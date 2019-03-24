from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'M2P'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'esports/', views.esports, name='esports'),
    url(r'events/', views.event, name='event'),
    url(r'localitzacio/', views.localitzacio, name='localitzacio'),
    url(r'amics/', views.amics, name='amics'),

    path('signup/', views.SignUp.as_view(), name='signup'),

]