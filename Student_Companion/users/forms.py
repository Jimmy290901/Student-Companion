from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(UserCreationForm):    
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control login-ip'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control login-ip'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Enrollment ID', 'class':'form-control login-ip'}),            
        }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control login-ip'
        self.fields['password2'].widget.attrs['class'] = 'form-control login-ip'
    

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['gender', 'phone_number', 'college_mail', 'major', 'enr_year']
        widgets = {
            'gender': forms.Select(attrs={'class':'form-control login-ip'}),
            'phone_number': forms.TextInput(attrs={'placeholder':'Phone', 'class':'form-control login-ip'}),
            'college_mail': forms.EmailInput(attrs={'placeholder':'College Email', 'class':'form-control login-ip'}),
            'major': forms.Select(attrs={'class':'form-control login-ip'}),
            'enr_year': forms.NumberInput(attrs={'placeholder':'Enrollment Year', 'class':'form-control login-ip'})
        }