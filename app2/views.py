from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def srujana(req):
    return HttpResponse('<b>srujana tinnava ra</b>')

def jamp(req):
    return HttpResponse('<h2>jampalakidi jaru mitaya')