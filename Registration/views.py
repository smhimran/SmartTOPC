from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from Registration.models import Student
from django.contrib import messages
from Registration.forms import Form, UserForm

# Create your views here.
def home(request):
    # dict = {'home': home}
    return render(request, 'Registration/home.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_staff = True
            user.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()

    dict = {
        'user_form':user_form,
        'registered':registered,
    }

    return render(request, 'Registration/register.html', context=dict)

@login_required
def list(request):
    student_list = Student.objects.order_by('ID')
    dict = {'table': student_list}
    return render(request, 'Registration/list.html', context=dict)

@login_required
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

def user_login(request):
    # username = None
    # password = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        else:
            return HttpResponse('Invalid Username or Password!')

    else:
        print('Invalid user tried to login')
        return render(request, 'Registration/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
