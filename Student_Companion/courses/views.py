from django.db.models.fields import NullBooleanField
from django.shortcuts import get_object_or_404, render
from .forms import courseForm
from django.contrib.auth.decorators import login_required
from users.models import Person
from .models import *

# Create your views here.
def addCourse(request):
    form = courseForm()
    context = {
        'form':form
    }
    return render(request,'courses/courseForm.html', context)

@login_required(login_url='/login')
def listCourses(request):
    person = get_object_or_404(Person, user = request.user)
    fdp_courses = CourseEnrollment.objects.filter(person = person, category_allotted = "F")
    ger_courses = CourseEnrollment.objects.filter(person = person, category_allotted = "G")
    major_courses = CourseEnrollment.objects.filter(person = person, category_allotted = "M")
    elective_courses = CourseEnrollment.objects.filter(person = person, category_allotted = "E")
    # non_cat_courses = CourseEnrollment.objects.filter(person = person, category_allotted = NullBooleanField)
    context = {
        'fdp': fdp_courses,
        'ger': ger_courses,
        'major': major_courses,
        'elective': elective_courses,
    }
    return render(request, 'courses/userCourses.html', context)
