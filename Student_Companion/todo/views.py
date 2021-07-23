from django.shortcuts import render
from .forms import *
from .models import *
from users.models import Person
# Create your views here.

def listTasks(request):
    newTask = NewTaskForm()
    person = Person.objects.get(user=request.user)
    if request.method == 'POST':
        task = NewTaskForm(request.POST)
        if task.is_valid():
            created_task = task.save(commit=False)
            created_task.person = person
            created_task.save()
            print('Task created successfully.')
    tasksList = Tasks.objects.filter(person=person)
    context = {
        'form':newTask,
        'tasksList': tasksList,
    }
    return render(request, 'todo/tasks.html', context)

def updateTask(request, task_id):
    print(task_id)

def deleteTask(request, task_id):
    print(task_id)