from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Prived Medved')

def category(request):
    return HttpResponse('aebat')