from django import forms
from .models import Curso
from .models import Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ['nombre', 'puntos']



class CustomUserChangeForm(UserChangeForm):
    password = None  # Ocultamos el campo de contraseña

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']        

class RegistroUsuarioForm(UserCreationForm):
      email = forms.EmailField()

class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']