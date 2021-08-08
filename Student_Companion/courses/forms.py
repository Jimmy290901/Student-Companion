from crispy_forms.helper import *
from  django import forms
from django.forms.widgets import Widget
from .models import Course

class courseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper
        self.helper.form_method='post'
        self.helper.form_class='form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
