from django.conf.urls import url
from . import views

app_name = 'M2P'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'esports/', views.esports, name='esports'),
]