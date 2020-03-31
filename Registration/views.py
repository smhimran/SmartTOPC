from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  as auth_login, logout
from Registration.models import Student, User, UserProfileInfo
from django.contrib import messages
from Registration.forms import Form, UserForm, UserProfileInfoForm

# Create your views here.
def home(request):
    # dict = {'home': home}
    return render(request, 'Registration/home.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    dict = {
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered,
    }

    return render(request, 'Registration/register.html', context=dict)

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
