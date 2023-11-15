from django.http import HttpRequest
from django.shortcuts import render

def homepage(request: HttpRequest):
    return render(request, 'index.html')