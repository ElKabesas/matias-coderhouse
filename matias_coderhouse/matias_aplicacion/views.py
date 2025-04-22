from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm
from .forms import AvatarForm
from .models import Avatar
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm



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




class CursoUpdateView(UpdateView):
    model = Curso
    fields = ['nombre', 'puntos']  
    template_name = 'matias_aplicacion/editar_curso.html'
    success_url = '/listado/'  

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'matias_aplicacion/curso_confirm_delete.html'
    success_url = reverse_lazy('listado_cursos')  # redirige después de eliminar



@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # o cualquier página de éxito
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'matias_aplicacion/editar_perfil.html', {'form': form})



@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user

            # Eliminar avatares anteriores del usuario (opcional)
            Avatar.objects.filter(user=request.user).delete()

            avatar.save()
            return redirect('inicio')
    else:
        form = AvatarForm()

    return render(request, 'matias_aplicacion/agregar_avatar.html', {'form': form})
