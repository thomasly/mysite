from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "personalsite/index.html", {})


def myintro(request):
    return HttpResponse("My name is Yang.")
