from django.shortcuts import render
from Registration.models import Student

# Create your views here.
def index(request):
    student_list = Student.objects.order_by('ID')
    dict = {'table': student_list}
    return render(request, 'Registration/list.html', context=dict)
