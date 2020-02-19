from django.db import models

# Create your models here.
class Student(models.Model):
    dept = (
        ('Cse', "CSE"),
        ('Soft', 'SWE'),
        ('cis', 'CIS'),
        ('other', 'Other'),
    )
    camp = (
        ('Main', 'MC'),
        ('Uttara', 'UC'),
    )
    sem = (
        ('first', '1st'),
        ('second', '2nd'),
    )
    shft = (
        ('day', 'Day'),
        ('eve', 'Evening'),
    )
    sec = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('e', 'E'),
    )
    tshirt = (
        ('mid', 'M'),
        ('large', 'L'),
        ('xlarge', 'XL'),
        ('xxlarge', 'XXL'),
        ('xxxlarge', 'XXXL'),
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
