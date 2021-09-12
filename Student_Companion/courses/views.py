from django.db.models.fields import NullBooleanField
from django.http import response
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from users.models import Person
from .models import *

# Create your views here.

@login_required(login_url='/login')
@staff_member_required
def addCourse(request):
    form=courseForm()
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form
    }
    return render(request,'courses/courseForm.html', context)

@login_required(login_url='/login')
@staff_member_required
def addFaculty(request):
    form=facultyForm()
    if request.method == 'POST':
        form = facultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form,      
    }
    return render(request,'courses/facultyForm.html', context)
 
@login_required(login_url='/login')
def listCourses(request):
    person = get_object_or_404(Person, user = request.user)
    fdp_courses = CourseEnrollment.objects.filter(person = person, category_allotted = "F", completed=True)
    ger_courses = CourseEnrollment.objects.filter(person = person, category_allotted = "G", completed=True)
    major_courses = CourseEnrollment.objects.filter(person = person, category_allotted = "M", completed=True)
    elective_courses = CourseEnrollment.objects.filter(person = person, category_allotted = "E", completed=True)

    completed_courses = CourseEnrollment.objects.filter(person = person, category_allotted = None, completed=True)
    incompleted_courses = CourseEnrollment.objects.filter(person = person, completed=False)

    courseAllotment = courseAllotForm()
    # non_cat_courses = CourseEnrollment.objects.filter(person = person, category_allotted = NullBooleanField)
    context = {
        'fdp': fdp_courses,
        'ger': ger_courses,
        'major': major_courses,
        'elective': elective_courses,
        
        'fdp_credits_user': person.fdp_credits_completed,
        'ger_credits_user': person.ger_credits_completed,
        'major_credits_user': person.major_credits_completed,
        'elective_credits_user': person.freeElectives_credits_completed,

        'fdp_credits_limit': person.major.fdp_credits,
        'ger_credits_limit': person.major.ger_credits,
        'major_credits_limit': person.major.major_credits,
        'elective_credits_limit': person.major.freeElectives_credits,

        'complete': completed_courses,
        'incomplete': incompleted_courses,

        'courseAllotment': courseAllotment,
    }
    return render(request, 'courses/userCourses.html', context)

@login_required(login_url='/login')
def allotCategory(request, course_ID, person_ID):    
    course = get_object_or_404(Course, course_ID = course_ID)
    person = get_object_or_404(Person, user = request.user)
    if request.user.username != person_ID:
        raise PermissionDenied
    if request.method == 'POST':
        original_obj = get_object_or_404(CourseEnrollment, course=course, person=person)
        prev_cat = original_obj.category_allotted
        saved_obj = courseAllotForm(request.POST).save(commit=False)
        original_obj.category_allotted = saved_obj.category_allotted
        original_obj.save()
        new_cat = original_obj.category_allotted
    
        if prev_cat == 'F':
            person.fdp_credits_completed -= course.credits
        elif prev_cat == 'G':
            person.ger_credits_completed -= course.credits
        elif prev_cat == 'M':
            person.major_credits_completed -= course.credits
        elif prev_cat == 'E':
            person.freeElectives_credits_completed -= course.credits
        
        if new_cat == 'F':
            person.fdp_credits_completed += course.credits
        elif new_cat == 'G':
            person.ger_credits_completed += course.credits
        elif new_cat == 'M':
            person.major_credits_completed += course.credits
        elif new_cat == 'E':
            person.freeElectives_credits_completed += course.credits
        
        person.save()
        return redirect('listCourses')
    
def displayCourse(request, course_ID):
    person = Person.objects.get(user=request.user)
    course = get_object_or_404(Course, course_ID = course_ID)
    if request.method == 'POST':
        my_obj = CourseEnrollment.objects.get(course=course, person=person)
        rating_form = ratingsForm(request.POST, instance=my_obj)
        if rating_form.is_valid():
            obj = rating_form.save(commit=False)            
            obj.review_d_and_t = timezone.now()
            course.total_reviews += 1
            course.avg_teaching_rating += (obj.teaching_rating - course.avg_teaching_rating)/(course.total_reviews)
            course.avg_syllabus_rating += (obj.syllabus_rating - course.avg_syllabus_rating)/(course.total_reviews)
            course.avg_material_rating += (obj.material_rating - course.avg_material_rating)/(course.total_reviews)
            obj.save()
            course.save()            
    students = CourseEnrollment.objects.filter(feedback__gt='', course = course).order_by('-review_d_and_t')
    avgRating = round((course.avg_teaching_rating + course.avg_syllabus_rating + course.avg_material_rating)/3,1)
    student_user = CourseEnrollment.objects.filter(course=course, person=person, review_d_and_t=None)
    if student_user:
        show_rate_btn = True
    else:
        show_rate_btn = False
    rating_form = ratingsForm()
    context = {
        'course': course,
        'avgRating': avgRating,
        'avgRatingRange': range(int(avgRating)),
        'remAvgRange': range(5- int(avgRating)),
        'avgTeachingRange': range(int(course.avg_teaching_rating)),
        'remTeachingRange': range(5- int(course.avg_teaching_rating)),
        'avgSyllabusRange': range(int(course.avg_syllabus_rating)),
        'remSyllabusRange': range(5- int(course.avg_syllabus_rating)),
        'avgMaterialRange': range(int(course.avg_material_rating)),
        'remMaterialRange': range(5- int(course.avg_material_rating)),
        'students': students,
        'show_rate_btn': show_rate_btn,
        'rating_form': rating_form,
    }

    return render(request, 'courses/courseDisplay.html', context)

@login_required(login_url='/login')
@staff_member_required
def enroll(request):
    enrollForm = enrollStudentForm()
    message = None
    if request.method == 'POST':
        enrollForm = enrollStudentForm(request.POST)
        if enrollForm.is_valid():
            obj = enrollForm.save(commit=False)
            old_obj = CourseEnrollment.objects.filter(course = obj.course, person=obj.person)
            if old_obj:
                message = "Student already enrolled."
            else:
                obj.save()
                message = "Student Enrollment successful."
        else:
            message = enrollForm.errors
    context = {
        'form': enrollForm,
        'message': message,
    }
    return render(request, "courses/enrollStudent.html", context)