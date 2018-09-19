from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")

def subpage1(request):
    return HttpResponse("This is subpage nr1")

# Create your views here.
