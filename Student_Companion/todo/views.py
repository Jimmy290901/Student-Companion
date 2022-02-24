from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from users.models import Person
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def listTasks(request):
    newTask = TaskForm()
    person = get_object_or_404(Person, user=request.user)
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            created_task = task.save(commit=False)
            created_task.person = person
            created_task.save()
            print('Task created successfully.')
            return redirect('/todo')
    tasksList = Tasks.objects.filter(person=person).order_by('-d_and_t')
    context = {
        'form':newTask,
        'tasksList': tasksList,
        'curr_date': datetime.now(),
    }
    return render(request, 'todo/tasks.html', context)

@login_required(login_url='/login')
def updateTask(request, task_id):
    if request.method == 'POST':
        person = get_object_or_404(Person, user = request.user)
        task = get_object_or_404(Tasks, id = task_id)
        if person != task.person:
            raise PermissionDenied
        task = TaskForm(request.POST)
        if task.is_valid():
            saved_obj = task.save(commit=False)
            original_obj = Tasks.objects.get(id = task_id)
            original_obj.task_desc = saved_obj.task_desc
            original_obj.completed = saved_obj.completed
            original_obj.rem_d_and_t = saved_obj.rem_d_and_t
            original_obj.save()
            print('Task updation complete!')
        else:
            print(task.errors)
    return redirect('/todo')

@login_required(login_url='/login')
def deleteTask(request, task_id):
    person = get_object_or_404(Person, user = request.user)
    task = get_object_or_404(Tasks, id = task_id)
    if person != task.person:
        raise PermissionDenied
    task.delete()
    return redirect('/todo')

@login_required(login_url='/login')
def changeStatus(request, task_id):
    person = get_object_or_404(Person, user = request.user)
    task = get_object_or_404(Tasks, id = task_id)
    if person != task.person:
        raise PermissionDenied
    else:
        task.completed = not task.completed
        task.save()
        return redirect('/todo')
