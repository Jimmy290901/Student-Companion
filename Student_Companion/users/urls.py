from django.contrib.auth import logout
from users.views import *
from django.urls import path

urlpatterns = [
    path('', home),
    path('login',login),
    path('signup',signup),
    path('logout',logout),
]