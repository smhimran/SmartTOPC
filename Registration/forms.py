from django import forms
from django.core import validators
from Registration.models import Student

class Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
