from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE
from django.utils import timezone
from users.models import Person
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.

class Faculty(models.Model):
    faculty_ID = models.IntegerField(primary_key=True)
    faculty_name = models.CharField(max_length=100)
    faculty_photo = models.ImageField(upload_to='Faculty', blank = True, null = True)
    faculty_mail = models.EmailField(max_length = 300)

    def __str__(self):
        return self.faculty_name
    

class Course(models.Model):
    course_ID = models.CharField(max_length = 10, primary_key=True)
    faculties = models.ManyToManyField(Faculty)
    course_photo = models.ImageField(upload_to='Course', default='Samples/Sample_Image.jpg', blank=True)
    course_title = models.CharField(max_length=100)
    credits = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank = True, null = True)
    objectives = models.TextField(blank = True, null = True)
    pedagogy = models.TextField(blank = True, null = True)
    expectation = models.TextField(blank = True, null = True)
    textbook = models.TextField(blank = True, null = True)
    reference_book = models.TextField(blank = True, null = True)
    passFail_course = models.BooleanField(default = False)
    project_details = models.TextField(blank = True, null = True)
    avg_teaching_rating = models.DecimalField(max_digits = 2, decimal_places=1, default=0.0)
    avg_syllabus_rating = models.DecimalField(max_digits = 2, decimal_places=1, default=0.0)
    avg_material_rating = models.DecimalField(max_digits = 2, decimal_places=1, default=0.0)
    prerequisite_courses = models.ManyToManyField("self", blank=True)
    antirequisite_courses = models.ManyToManyField("self", blank=True)
    total_reviews = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.course_ID
    
    def dispPgURL(self):
        return reverse('displayCourse', kwargs={'course_ID': self.course_ID})

class CourseEnrollment(models.Model):
    class Meta:
        UniqueConstraint(fields=('Course','Person'), name='primary_key')
    category_choices = (
        ("F", "Foundation Programme"),
        ("G", "General Education Requirements"),
        ("M", "Major Course"),
        ("E", "Free Electives")
    )
    ratings_choices = (
        (0,"0"),
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5")
    )
    course = models.ForeignKey(Course, on_delete=CASCADE)
    person = models.ForeignKey(Person, on_delete=CASCADE)
    completed = models.BooleanField(default=False)
    reg_d_and_t = models.DateTimeField(default = timezone.now)
    teaching_rating = models.IntegerField(null=True, blank=True, choices=ratings_choices)
    syllabus_rating = models.IntegerField(null=True, blank=True, choices=ratings_choices)
    material_rating = models.IntegerField(null=True, blank=True, choices=ratings_choices)
    feedback = models.TextField(null=True, blank=True)
    review_d_and_t = models.DateTimeField(null=True, blank=True)
    category_allotted = models.CharField(max_length = 1, null=True,blank=True,choices=category_choices)

    def __str__(self):
        return (self.person.user.username + " -> " + self.course.course_ID)
    
    def categoryAllotURL(self):
        return reverse('allotCategory', kwargs={'course_ID':self.course.course_ID, 'person_ID': self.person.user.username})
    
