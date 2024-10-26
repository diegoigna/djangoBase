from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('todo/', views.todo, name='todo'),
     path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    ]