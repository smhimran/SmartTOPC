from django import forms

class Form(forms.Form):
    ID = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
