from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(UserCreationForm):    
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Enrollment ID'}),
        }
    

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['gender', 'phone_number', 'college_mail', 'major', 'enr_year']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder':'Phone'}),
            'college_mail': forms.EmailInput(attrs={'placeholder':'College Email'}),
            'enr_year': forms.NumberInput(attrs={'placeholder':'Enrollment Year'})
        }