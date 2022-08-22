from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def aboutMe(request):
    
        return render(request,"appAboutMe/inicio.html")
    
