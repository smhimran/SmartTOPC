from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    dept = (
        ('CSE', "CSE"),
        ('SWE', 'SWE'),
        ('CIS', 'CIS'),
        ('Other', 'Other'),
    )
    camp = (
        ('MC', 'MC'),
        ('UC', 'UC'),
    )
    sem = (
        ('1st', '1st'),
        ('2nd', '2nd'),
    )
    shft = (
        ('Day', 'Day'),
        ('Evening', 'Evening'),
    )
    sec = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    tshirt = (
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    )

    ID = models.CharField(max_length=20, unique=True, primary_key=True)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=10, choices=dept, default='Cse')
    Campus = models.CharField(max_length=10, choices=camp, default='Main')
    Semester = models.CharField(max_length=10, choices=sem, default='first')
    Shift = models.CharField(max_length=10, choices=shft, default='day')
    Section = models.CharField(max_length=10, choices=sec)
    TShirt = models.CharField(max_length=10, choices=tshirt, default='mid')
    Status = models.BooleanField(default=False)
    # Token = models.AutoField(auto_created=True, unique=True, default=1001, serialize=True)

    def __str__(self):
        return self.ID

class Contestant(models.Model):
    Token = models.AutoField(auto_created=True, primary_key=True, unique=True, serialize=True)
    ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    # Name = models.ForeignKey(Student, on_delete=models.CASCADE)
    TShirt = models.CharField(max_length=10, choices=Student.tshirt, default='mid')

    def __str__(self):
        return str(self.Token)
