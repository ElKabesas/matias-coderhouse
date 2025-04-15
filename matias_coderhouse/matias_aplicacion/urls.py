from django.urls import path
from . import views
from .views import CursoUpdateView


urlpatterns = [
    path('', views.listado_cursos, name='inicio'),
    path('listado/', views.listado_cursos, name='listado_cursos'),
    path('crear/', views.crear_curso, name='crear_curso'),
    path('curso/<int:pk>/', views.CursoDetalleView.as_view(), name='detalle_curso'),
    path('curso/editar/<int:pk>/', CursoUpdateView.as_view(), name='editar_curso'),

]