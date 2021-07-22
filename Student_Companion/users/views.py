from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from .forms import *

# Create your views here.

user_navbar = {
    'Home': '',
    'To-Do': '',
    'Your Courses': '',
    'Rate Courses': '',
    'Resume Maker': ''
}

admin_navbar = {
    'Home':'',
    'Add Courses':'',
    'Enroll Students':'',
}

def home(request):
    context = {
        'navbar_links': admin_navbar
    }
    return render(request, 'users/home.html', context)

def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            message = 'Login Successfull'
        else:
            message = 'Login Unsuccessfull'
    context = {
        'message': message
    }
    return render(request, 'users/login.html', context)

def signup(request):
    person = PersonForm()
    user = UserForm()
    if request.method == 'POST':
        user = UserForm(request.POST)
        person = PersonForm(request.POST)
        if user.is_valid() and person.is_valid():
            created_user = user.save()
            created_person = person.save(commit = False)
            created_person.user = created_user
            created_person.save()
            print('User created successfully')
            return redirect('login')

    context = {
        'user_form':user,
        'person_form':person,
        'user_error':user.errors,
        'person_error':person.errors,
    }
    return render(request,'users/signup.html', context)