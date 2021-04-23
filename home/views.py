import webbrowser

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    webbrowser.open("./dist/dist/index.html")
    return HttpResponse("Hello, world. You're at the polls index.")
