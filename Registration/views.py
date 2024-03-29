from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from Registration.models import Student, Contestant
from django.db.models import Q, Max
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

@login_required
def dashboard(request):
    #Students info
    registered = Student.objects.filter(Status=True).count()
    not_registered = Student.objects.filter(Status=False).count()

    #Departments
    cse = Contestant.objects.filter(basic_info__Department='CSE').count()
    swe = Contestant.objects.filter(basic_info__Department='SWE').count()
    cis = Contestant.objects.filter(basic_info__Department='CIS').count()
    other = Contestant.objects.filter(basic_info__Department='Other').count()

    #Campus
    mc = Contestant.objects.filter(basic_info__Campus='MC').count()
    uc = Contestant.objects.filter(basic_info__Campus='UC').count()

    #Semester
    first = Contestant.objects.filter(basic_info__Semester='1st').count()
    second = Contestant.objects.filter(basic_info__Semester='2nd').count()

    #T-Shirt
    m = Contestant.objects.filter(TShirt='M').count()
    l = Contestant.objects.filter(TShirt='L').count()
    xl = Contestant.objects.filter(TShirt='XL').count()
    xxl = Contestant.objects.filter(TShirt='XXL').count()
    xxxl = Contestant.objects.filter(TShirt='XXXL').count()

    dict = { 'registered':registered, 'not_registered':not_registered,
            'cse':cse, 'swe':swe, 'cis':cis, 'other':other,
            'mc':mc, 'uc':uc,
            'first':first, 'second':second,
            'm':m, 'l':l, 'xl':xl, 'xxl':xxl, 'xxxl':xxxl,
            }
    return render(request, 'Registration/dashboard.html', context=dict)

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
    if request.user.is_superuser == 0:
        return HttpResponseRedirect(reverse('home'))
    student_list = Student.objects.order_by('ID')
    dict = {'table': student_list}
    return render(request, 'Registration/list.html', context=dict)

@login_required
def contestants(request):
    reg_std = Contestant.objects.order_by('Token')
    dict = {'table': reg_std}
    return render(request, 'Registration/reg_std.html', context=dict)

@login_required
def user_entry(request):
    if request.user.is_superuser == 0:
        return HttpResponseRedirect(reverse('home'))
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
            return redirect('user_login')

    else:
        # print('Invalid user tried to login')
        return render(request, 'Registration/login.html')

@login_required
def reg_std(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        department = request.POST.get('department')
        campus = request.POST.get('campus')
        semester = request.POST.get('semseter')
        shift = request.POST.get('shift')
        section = request.POST.get('section')
        tShirt = request.POST.get('tshirt')



        student = Student.objects.get(ID=id)

        print('ID = {} Name = {}'.format(str(student.ID), str(student.Name)))

        if student.Status == True:
            contestant = Contestant.objects.get(ID=id)

            contestant.TShirt = tShirt

            student.Name = name
            student.Department = department
            student.Campus = campus
            student.Semester = semester
            student.Shift = shift
            student.Section = section

            student.save()
            contestant.basic_info = student

            contestant.save()
            return HttpResponseRedirect(reverse('home'))

        else:
            token = 0
            mx = Contestant.objects.order_by('-Token').first()
            if mx == None:
                token = 1000
            else:
                token = mx.Token
            token += 1


            student.Status = True
            student.Name = name
            student.Department = department
            student.Campus = campus
            student.Semester = semester
            student.Shift = shift
            student.Section = section

            student.save()

            contestant = Contestant.objects.create(
                basic_info = student,
                TShirt = tShirt,
                Token = token,
            )


            contestant.save()

            return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
