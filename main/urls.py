from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('concluidas', views.tasks_ok, name='tasks_ok'),
      path('pendentes', views.tasks_nok, name='tasks_nok'),
      path('nova/', views.create_task, name='create_task'),
      path('update/<int:id>/', views.update_task, name='update_task'),
      path('deletar/<int:id>/', views.deletar_task, name='deletar_task'),
      path('taks/', views.task_list_prioridade, name='task_list_prioridade'),
]