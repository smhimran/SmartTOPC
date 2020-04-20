import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SmartTOPC.settings')

import django
django.setup()

# Fake scripts
import random
from Registration.models import Student
from faker import Faker

fake = Faker()

def gen_student():
    d = ['CSE', 'SWE', 'CIS', 'Other']
    c = ['MC', 'UC']
    sem = ['1st', '2nd']
    shi = ['Day', 'Evening']
    sec = ['A', 'B', 'C', 'D', 'E']
    t = ['M', 'L', 'XL', 'XXL', 'XXXL']
    st = [False, True]
    name = fake.name()
    department = random.choices(d)[0]
    campus = random.choices(c)[0]
    semester = random.choices(sem)[0]
    shift = random.choices(shi)[0]
    section = random.choices(sec)[0]
    # tShirt = random.choices(t)[0]
    # status = False
    s = Student.objects.get_or_create(ID='193-15-'+str(random.randint(11000, 25000)), Name=name, Department=department, Campus=campus, Semester=semester, Shift=shift, Section=section)[0]

    s.save()


def gen(n):
    for i in range(n):
        gen_student()


if __name__ == '__main__':
    print('Generating...Please wait....')
    gen(120)
    print('Done :)')
