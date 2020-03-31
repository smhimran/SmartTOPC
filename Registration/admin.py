from django.contrib import admin
from Registration.models import *
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Department', 'Campus', 'Semester', 'Shift', 'Section', 'TShirt', 'Status')

class contestantAdmin(admin.ModelAdmin):
    list_display = ('Token', 'ID',  'TShirt')


admin.site.register(Student, studentAdmin)
admin.site.register(Contestant, contestantAdmin)
admin.site.register(UserProfileInfo)
