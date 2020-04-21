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

    ID = models.CharField(max_length=20, unique=True, primary_key=True)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=10, choices=dept, default='CSE')
    Campus = models.CharField(max_length=10, choices=camp, default='MC')
    Semester = models.CharField(max_length=10, choices=sem, default='1st')
    Shift = models.CharField(max_length=10, choices=shft, default='Day')
    Section = models.CharField(max_length=10, choices=sec)
    Status = models.BooleanField(default=False)
    # Token = models.AutoField(auto_created=True, unique=True, default=1001, serialize=True)

    def __str__(self):
        return self.ID

class Contestant(models.Model):

    basic_info = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    # ID = models.CharField(max_length=20, unique=True)
    # Name = models.CharField(max_length=50, default='No name')
    # Department = models.CharField(max_length=10, default='CSE')
    # Campus = models.CharField(max_length=10, default='MC')
    # Semester = models.CharField(max_length=10, default='1st')
    # Shift = models.CharField(max_length=10, default='Day')
    # Section = models.CharField(max_length=10, default='A')
    TShirt = models.CharField(max_length=10, default='M')
    Token = models.IntegerField(primary_key=True, default=1001)
    # Contestant_Name = models.ForeignKey(Student, on_delete=models.CASCADE)

    @property
    def id(self):
        return str(self.basic_info.ID)

    def name(self):
        return str(self.basic_info.Name)

    def dept(self):
        return str(self.basic_info.Department)

    def __str__(self):
        return str(self.Token)
