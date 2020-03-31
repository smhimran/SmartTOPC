from django import forms
from django.core import validators
from django.contrib.auth.models import User
from Registration.models import Student, UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic', )


class Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
