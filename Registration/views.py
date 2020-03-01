from django.shortcuts import render
from Registration.models import Student
from . import forms

# Create your views here.
def index(request):
    student_list = Student.objects.order_by('ID')
    dict = {'table': student_list}
    return render(request, 'Registration/list.html', context=dict)

def form_view(request):
    form = forms.Form()
    return render(request, 'Registration/form_page.html', {'form': form})
