from django import forms
from.models import Equipo,Proyecto, Tarea

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['descripcion', 'fecha_inicio', 'fecha_termino', 'responsable', 'ejecutor']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_termino': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }