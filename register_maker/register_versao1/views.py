from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My App </em>")


def cadastro(request):
    return HttpResponse("<h1>URL: Cadastro2</h1>")