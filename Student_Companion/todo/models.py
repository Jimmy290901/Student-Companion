from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE
from users.models import Person
from django.utils import timezone
# Create your models here.

class Tasks(models.Model):
    person = models.ForeignKey(Person, on_delete=CASCADE)
    task_desc = models.CharField(max_length=500)
    completed = models.BooleanField(default = False)
    d_and_t = models.DateTimeField(default = timezone.now)
    rem_d_and_t = models.DateTimeField(blank =True, null = True)

    def update_url(self):
        return reverse('updateTask',kwargs={'task_id':self.id})
    def delete_url(self):
        return reverse('deleteTask', kwargs={'task_id':self.id})