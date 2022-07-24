from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse('vista inicio')

def fabricas(request):
    return HttpResponse('vista fabricas')

def clientes(request):
    return HttpResponse('vista clientes')

def hilados(request):
    return HttpResponse('vista hilados')


