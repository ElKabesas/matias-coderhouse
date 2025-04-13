
  
from django.urls import path
from . import views


urlpatterns = [
    path('', views.listado, name='inicio'),  # Esta es la raíz del sitio
    path('listado/', views.listado, name='listado'),
    path('crear-curso/', views.crear_curso, name='crear_curso'),
]
