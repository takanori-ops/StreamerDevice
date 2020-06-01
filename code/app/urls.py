from django.urls import path
from . import views


urlpatterns = [
    path('list/',views.card,name='card'),
    path('home/',views.home,name='home')
]