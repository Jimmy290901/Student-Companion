from datetime import datetime
from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_desc','rem_d_and_t','completed']
        widgets = {
            'task_desc': forms.TextInput(attrs={'placeholder':'Eg. Do Laundry'}),
            'rem_d_and_t': forms.DateTimeInput(attrs={'type':'datetime-local', 'placeholder':'Reminder'})
        }