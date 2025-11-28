from django.shortcuts import render, redirect, get_object_or_404
from main.models import Task
from main.forms import TaskForm


def task_list(request):
    tarefas = Task.objects.all()
    context = {
        'tarefas':tarefas
    }
    
    return render(request, 'tasks/task_list.html', context)

def tasks_ok(request):
    
    tarefas = Task.objects.filter(concluida=1)
    context = {
        'tarefas': tarefas
    }
    
    return render(request, 'tasks/tasks_ok.html', context)

def tasks_nok(request):
    
    tarefas = Task.objects.filter(concluida=0)
    context = {
        'tarefas': tarefas
    }
    
    return render(request, 'tasks/tasks_ok.html', context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        
    else:
        form = TaskForm()
            
    context = {'form': form}
    return render(request, 'tasks/task_form.html', context)

#Atualizar tabela

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

#deletar objeto da lista

def deletar_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')