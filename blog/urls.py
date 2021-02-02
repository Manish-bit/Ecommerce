from django.urls import path
from . import  views

urlpatterns =[path("blog/",views.myview,name = "index")]