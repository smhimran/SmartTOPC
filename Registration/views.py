from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from Registration.models import Student
from django.db.models import Q
from django.contrib import messages
from Registration.forms import Form, UserForm

# Create your views here.
def home(request):
    # dict = {'home': home}
    model = Student
    result = None
    # def get_queryset(self):
    #    # result = super(home, self).get_queryset()

    #
    #    return result

    if request.method == "POST":
        query = request.POST.get('search')
        if query:
           result = Student.objects.filter(Q(ID__contains=query) | Q(Name__contains=query))
        else:
            result = None
        # result = super(self, home).get_queryset()
    # result = Student.objects.all()
    dict = {'result':result}
    return render(request, 'Registration/home.html', context=dict)

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
            messages.error(request, 'Invalid Username or Password!')
            return redirect('Registration:user_login')

    else:
        # print('Invalid user tried to login')
        return render(request, 'Registration/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
