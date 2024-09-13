from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def xd(request):
    return HttpResponse("<h1>Soy de la appnacho</h1>")

def oe(request):
    html="""
        <h1 style="color:blue">hola mundo</h1>
        <p>Soy un subtitulo</p>
        """
    
    return HttpResponse(html)