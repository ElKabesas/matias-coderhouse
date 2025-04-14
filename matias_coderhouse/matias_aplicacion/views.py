from django.shortcuts import render, redirect
from .forms import CursoForm
from .models import Curso  # importo el modelo

# mostrar todos los cursos
def listado(request):
    cursos = Curso.objects.all()
    return render(request, 'matias_aplicacion/listado.html', {'cursos': cursos})

# página de inicio
def inicio(request):
    return render(request, 'matias_aplicacion/inicio1.html')

# crear un curso
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado')
    else:
        form = CursoForm()
    return render(request, 'matias_aplicacion/crear_curso.html', {'form': form})