from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

class Major(models.Model):
    programme_name = models.CharField(max_length=200)
    fdp_credits = models.IntegerField()
    ger_credits = models.IntegerField()
    major_credits = models.IntegerField()
    freeElectives_credits = models.IntegerField()
    durationYr = models.IntegerField()

    def __str__(self):
        return self.programme_name

class Person(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'I prefer not to say')
    )
    user = models.OneToOneField(User, on_delete=CASCADE)
    gender = models.CharField(max_length = 1, choices=gender_choices)
    phone_number = models.CharField(max_length=10)
    college_mail = models.EmailField()
    major = models.ForeignKey(Major, on_delete=CASCADE)
    enr_year = models.IntegerField(validators=[MaxValueValidator(timezone.now().year)])
    fdp_credits_completed = models.IntegerField(default = 0)
    ger_credits_completed = models.IntegerField(default = 0)
    major_credits_completed = models.IntegerField(default = 0)
    freeElectives_credits_completed = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username