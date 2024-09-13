from django.shortcuts import render
from django.http import HttpResponse


def vista_1(request):
    return HttpResponse("Wena esta el la primera vista del app del vistor XD")

def vista_2(request):
    return HttpResponse("Chao esta es la segunda vista de la app o.o .")
