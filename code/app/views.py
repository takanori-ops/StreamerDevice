from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render


def index(request):
    urlName = reverse('index')
    return HttpResponse("Hello, world. You're at the polls index.{0}".format(urlName))


def home(request):
    return render(request,'public/home.html')

def card(request):
    return render(request,'public/card.html')
