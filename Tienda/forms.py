from django import forms
from .models import Compania,Plataforma,Genero,Juego

class CompaniaForm(forms.ModelForm):
    class Meta:
        model=Compania
        fields=['nombre_compania']
        widgets={
            'nombre_compania':forms.TextInput(attrs={'class':'form-control',
                                             'placeholder':'Nombre Compania'}),
        }
class PlataformaForm(forms.ModelForm):
    class Meta:
        model=Plataforma
        fields=['nombre_plataforma']
        widgets={
            'nombre_plataforma':forms.TextInput(attrs={'class':'form-control',
                                             'placeholder':'Nombre Plataforma'}),
        }
class GeneroForm(forms.ModelForm):
    class Meta:
        model=Genero
        fields=['nombre_genero']
        widgets={
            'nombre_genero':forms.TextInput(attrs={'class':'form-control',
                                             'placeholder':'Nombre Genero'}),
        }
class JuegoForm(forms.ModelForm):
    class Meta:
        model=Juego
        fields=['titulo','foto','compania','plataforma','genero','precio']
