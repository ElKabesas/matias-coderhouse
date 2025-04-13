from django.shortcuts import render, redirect
from .forms import CursoForm

# Create your views here.
from django.http import HttpResponse

def listado(request):
    return render(request, 'matias_aplicacion/listado.html')
def inicio(request):
    return render(request, 'matias_aplicacion/inicio1.html')


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado')  # este nombre sí existe en urls.py
    else:
        form = CursoForm()

    return render(request, 'matias_aplicacion/crear_curso.html', {'form': form})
