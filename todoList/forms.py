from django import forms
from .models import todoList


class TaskForm(forms.ModelForm):
    class Meta:
        model = todoList
        fields = ['task_name']
        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add a new task"
            })
        }
