from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  as auth_login, logout
from Registration.models import Student
from django.contrib import messages
from Registration.forms import Form

# Create your views here.
def home(request):
    # dict = {'home': home}
    return render(request, 'Registration/home.html')

def list(request):
    student_list = Student.objects.order_by('ID')
    dict = {'table': student_list}
    return render(request, 'Registration/list.html', context=dict)

def user_entry(request):
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("Invalid Data")
    else:
        return render(request, 'Registration/form_page.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
