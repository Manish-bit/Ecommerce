from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    return HttpResponse("Hello Shop")
# Create your views here.
# New views
