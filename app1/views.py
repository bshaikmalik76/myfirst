from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def malik(reg):
    return HttpResponse('<marquee><h1>malik is innocent</marquee></h1>')

def baby(req):
    return HttpResponse('<b><marquee>baby miss u</marquee></b>')