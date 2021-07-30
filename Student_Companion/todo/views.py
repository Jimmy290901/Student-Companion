from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from users.models import Person
from django.core.exceptions import PermissionDenied
# Create your views here.

def listTasks(request):
    newTask = NewTaskForm()
    person = get_object_or_404(Person, user=request.user)
    if request.method == 'POST':
        task = NewTaskForm(request.POST)
        if task.is_valid():
            created_task = task.save(commit=False)
            created_task.person = person
            created_task.save()
            print('Task created successfully.')
    tasksList = Tasks.objects.filter(person=person).order_by('-d_and_t')
    context = {
        'form':newTask,
        'tasksList': tasksList,
    }
    return render(request, 'todo/tasks.html', context)

def updateTask(request, task_id):
    print(task_id)

def deleteTask(request, task_id):
    person = get_object_or_404(Person, user = request.user)
    task = get_object_or_404(Tasks, id = task_id)
    if person != task.person:
        raise PermissionDenied
    task.delete()
    return redirect('/todo')
