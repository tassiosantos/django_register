from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me':"variável inserida pela função", 'insert_me2':123}
    return render(request,'register_versao1/index.html',context=my_dict)


def cadastro(request):
    return HttpResponse("<h1>URL: Cadastro2</h1>")
