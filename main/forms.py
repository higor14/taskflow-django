from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'data_limite', 'prioridade', 'concluida']
        
        widgets = {
        'data_limite': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        'prioridade': forms.Select(attrs={'class': 'form-control'
            
        })
        
        }