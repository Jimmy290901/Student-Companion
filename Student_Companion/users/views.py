from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import *
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def home(request):
    return render(request, 'users/home.html')

def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            message = 'Invalid Credentials. Try again.'
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
            # print('User created successfully')
            auth.login(request,created_user)
            return redirect('/')

    context = {
        'user_form':user,
        'person_form':person,
        'user_error':user.errors,
        'person_error':person.errors,
    }
    print(user.errors, person.errors)
    return render(request,'users/signup.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/login')