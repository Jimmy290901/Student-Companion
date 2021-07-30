from todo.views import *
from django.urls import path

urlpatterns = [
    path('', listTasks),
    path('updateTask/<int:task_id>', updateTask, name="updateTask"),
    path('deleteTask/<int:task_id>', deleteTask, name="deleteTask"),
]