from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def listado(request):
    return render(request, 'matias_aplicacion/listado.html')
def inicio(request):
    return render(request, 'matias_aplicacion/inicio1.html')