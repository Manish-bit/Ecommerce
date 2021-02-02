from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    return HttpResponse("Hello Blog")   

# Create your views here.
