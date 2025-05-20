from django.shortcuts import render
from django.http import HttpResponse


def Home(response):
    return HttpResponse("Hello and welcome to my website")
    
