from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView



def inicio(request):
    return render(request, 'matias_aplicacion/inicio1.html')

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_cursos')
    else:
        form = CursoForm()
    return render(request, 'matias_aplicacion/crear_curso.html', {'form': form})

def listado_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'matias_aplicacion/listado.html', {'cursos': cursos})

class CursoDetalleView(DetailView):
    model = Curso
    template_name = 'matias_aplicacion/index.html' 


from django.views.generic.edit import UpdateView
from .models import Curso

class CursoUpdateView(UpdateView):
    model = Curso
    fields = ['nombre', 'puntos']  
    template_name = 'matias_aplicacion/editar_curso.html'
    success_url = '/listado/'  

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'matias_aplicacion/curso_confirm_delete.html'
    success_url = reverse_lazy('lista_cursos')  # redirige después de eliminar
