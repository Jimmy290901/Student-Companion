from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import courseForm

# Create your views here.
def addCourse(request):
    form = courseForm()
    return render(request,'courses/courseForm.html',{'form':form})