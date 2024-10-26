from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404
from .models import Equipo, Proyecto, Tarea
from .forms import EquipoForm, ProyectoForm, TareaForm
# Create your views here.

def todo(request):
    proyectos = Proyecto.objects.all()  
    return render(request, 'todo.html', {'proyectos': proyectos})  

def inicio(request):
    if request.method == 'POST':
        equipo_form = EquipoForm(request.POST)
        proyecto_form = ProyectoForm(request.POST)
        tarea_form = TareaForm(request.POST)

        if equipo_form.is_valid() and proyecto_form.is_valid() and tarea_form.is_valid():
            equipo = equipo_form.save()
            proyecto = proyecto_form.save(commit=False)
            proyecto.equipo = equipo
            proyecto.save()

            tarea = tarea_form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()

            return redirect('todo')  # Redirige a la vista todo
    else:
        equipo_form = EquipoForm()
        proyecto_form = ProyectoForm()
        tarea_form = TareaForm()

    return render(request, 'inicio.html', {
        'equipo_form': equipo_form,
        'proyecto_form': proyecto_form,
        'tarea_form': tarea_form,
    })

def delete_project(request, project_id):
    try:
        proyecto = get_object_or_404(Proyecto, id=project_id)
        if request.method == 'POST':
            proyecto.delete()
            return redirect('todo')  
    except Http404:
        return redirect('todo')