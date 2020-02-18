from django.contrib import admin
from Registration.models import *
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Department', 'Campus', 'Semester', 'Shift', 'Section', 'TShirt', 'Status')

admin.site.register(Student, Admin)
