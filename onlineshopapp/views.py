from django.http import HttpRequest
from django.shortcuts import render

def homepage(request: HttpRequest):
    return render(request, 'index.html')
def techpage(request):
    return render(request, 'tech.html')
def fashionpage(request):
    return render(request, 'fashion.html')
def autopage(request):
    return render(request, 'auto.html')
def jewelrypage(request):
    return render(request, 'jewelry.html')
def foodpage(request):
    return render(request, 'food.html')