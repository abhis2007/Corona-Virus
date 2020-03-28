from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def prevention(request):
    return render(request,"prevention.html")

def symptoms(request):
    return render(request,"symptoms.html")

def graph(request):
    return render(request,"graph.html")