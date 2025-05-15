from django.urls import path
from . import views
from .views import CursoUpdateView
from .views import CursoDeleteView
from .views import editar_perfil
from .views import agregar_avatar
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views



urlpatterns = [
    path('', views.listado_cursos, name='inicio'),
    path('listado/', views.listado_cursos, name='listado_cursos'),
    path('crear/', views.crear_curso, name='crear_curso'),
    path('curso/<int:pk>/', views.CursoDetalleView.as_view(), name='detalle_curso'),
    path('curso/editar/<int:pk>/', CursoUpdateView.as_view(), name='editar_curso'),
    path('curso/eliminar/<int:pk>/', CursoDeleteView.as_view(), name='eliminar_curso'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
    path('agregar_avatar/', agregar_avatar, name='agregar_avatar'),
    path('login/', LoginView.as_view(template_name='matias_aplicacion/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about/', views.about, name='about'),
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('registro/', views.registro, name='registro'),




]