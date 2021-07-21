from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE
from django.utils import timezone
from users.models import Person
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Faculty(models.Model):
    faculty_ID = models.IntegerField(primary_key=True)
    faculty_name = models.CharField(max_length=100)
    faculty_photo = models.ImageField(upload_to='Faculty', blank = True, null = True)
    faculty_mail = models.EmailField(max_length = 300)

class Course(models.Model):
    course_ID = models.CharField(max_length = 10, primary_key=True)
    faculties = models.ManyToManyField(Faculty)
    credits = models.IntegerField()
    description = models.TextField(blank = True, null = True)
    objectives = models.TextField(blank = True, null = True)
    pedagogy = models.TextField(blank = True, null = True)
    expectation = models.TextField(blank = True, null = True)
    textbook = models.TextField(blank = True, null = True)
    refbook = models.TextField(blank = True, null = True)
    pf_allowed = models.BooleanField(default = False)
    project_details = models.TextField(blank = True, null = True)
    avg_rating = models.DecimalField(max_digits = 2, decimal_places=1, null=True, blank = True)
    prereq = models.ManyToManyField("self")
    antireq = models.ManyToManyField("self")

class CourseEnrollment(models.Model):
    class Meta:
        UniqueConstraint(fields=('Course','Person'), name='primary_key')
    category_choices = (
        ("F", "Foundation Programme"),
        ("G", "General Education Requirements"),
        ("M", "Major Course"),
        ("E", "Free Electives")
    )
    course = models.ForeignKey(Course, on_delete=CASCADE)
    person = models.ForeignKey(Person, on_delete=CASCADE)
    completed = models.BooleanField(default=False)
    reg_d_and_t = models.DateTimeField(default = timezone.now)
    teaching_rating = models.IntegerField(blank = True, null = True, validators = [MaxValueValidator(5), MinValueValidator(0)])
    syllabus_rating = models.IntegerField(blank = True, null = True, validators = [MaxValueValidator(5), MinValueValidator(0)])
    material_rating = models.IntegerField(blank = True, null = True, validators = [MaxValueValidator(5), MinValueValidator(0)])
    category_allotted = models.CharField(max_length = 1, null=True,blank=True,choices=category_choices)
