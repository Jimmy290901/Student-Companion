from crispy_forms.helper import *
from crispy_forms.layout import ButtonHolder, Submit
from  django import forms
from django.db.models.fields import CharField
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Course, CourseEnrollment, Faculty

class courseForm(forms.ModelForm):
    class Meta:
        model=Course
        exclude = ('avg_teaching_rating','avg_syllabus_rating','avg_material_rating','total_reviews'),

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method='post'
        self.helper.form_class='form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Add Course'))
        # self.helper.layout = Layout(
        #     ButtonHolder(
        #         Submit('submit', 'Add Course')
        #     )
        # )

class facultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields='__all__'
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method='post'
        self.helper.form_class='form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Add Faculty'))
        # self.helper.layout = Layout(
        #     ButtonHolder(
        #         Submit('submit', 'Add Faculty')
        #     )
        # )

class courseAllotForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = ('category_allotted',)

class ratingsForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = ('teaching_rating', 'syllabus_rating', 'material_rating', 'feedback')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['teaching_rating'].required = True
        self.fields['syllabus_rating'].required = True
        self.fields['material_rating'].required = True
        self.helper=FormHelper()
        self.helper.form_method='post'
        self.helper.form_class='form-horizontal'
        self.helper.form_id = 'ratings_form'
        self.helper.label_class = 'col-lg-2 unset-width'
        self.helper.field_class = 'col-lg-8 full-width'
        # self.helper.add_input(Submit('submit', 'Submit'))

class enrollStudentForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = ('course', 'person')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form_horizontal'
        # self.helper.label_class = 'col-lg-2'
        # self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Enroll'))