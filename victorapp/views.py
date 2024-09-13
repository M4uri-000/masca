from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista_1(request):
    return HttpResponse("<h1>hijolaperra</h1>")

def vista_2(request):
    html="""
        <p>hola carlita</p>
        <h2>no te acolday na</h2> 
    """
    return HttpResponse(html)