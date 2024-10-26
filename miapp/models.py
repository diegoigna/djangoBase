from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion= models.TextField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    descripcion=models.CharField(max_length=255)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    responsable= models.ForeignKey(User,  related_name='responsable_tareas', on_delete=models.CASCADE)
    ejecutor = models.ForeignKey(User, related_name='ejecutor_tares', on_delete =models.CASCADE)

    def __str__(self):
        return self.descripcion
    
    def duracion(self):
        return (self.fecha_termino - self.fecha_inicio).days