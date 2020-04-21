from django.contrib import admin
from Registration.models import *
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Department', 'Campus', 'Semester', 'Shift', 'Section', 'Status')

# def basic_info(self, object):
#     return object.contestant.student

class contestantAdmin(admin.ModelAdmin):
    model = Contestant
    list_display = ('Token', 'id', 'name', 'dept', 'TShirt')


admin.site.register(Student, studentAdmin)
admin.site.register(Contestant, contestantAdmin)
