from  django import forms
from django.forms.widgets import Widget

class courseForm(forms.Form):
    name=forms.CharField(label='Course Name')
    course_ID = forms.CharField(max_length = 10, label='Course ID')
    faculties = forms.CharField(label='Faculty Name')
    credits = forms.DecimalField(max_value=4.0,label='Course Cresits')
    description = forms.CharField(required=False, widget=forms.Textarea, label='Course Description')
    objectives = forms.CharField(required=False,widget=forms.Textarea, label='Course Objectives')
    pedagogy = forms.CharField(required=False,widget=forms.Textarea, label='Course Pedagogy')
    expectation = forms.CharField(required=False,widget=forms.Textarea, label='Course Expectations')
    textbook = forms.CharField(required=False,widget=forms.Textarea, label='Course TextBooks')
    refbook = forms.CharField(required=False, widget=forms.Textarea, label='Course Reference Books')
    pf_allowed = forms.BooleanField(required=False, label='Pass/Fail Course?')
    project_details = forms.CharField(required=False,widget=forms.Textarea, label='Course Objectives')
    avg_rating = forms.DecimalField(max_value=5.0, decimal_places=1, required=False)
    prereq = forms.CharField()
    antireq = forms.CharField()