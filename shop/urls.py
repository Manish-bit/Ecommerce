from django.urls import path
from . import  views

urlpatterns =[path("shop/",views.myview,name = "index")]