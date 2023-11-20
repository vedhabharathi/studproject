from django.contrib import admin
from myapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Rollno', 'Name','Class','Gender','Age','Group','Address']
admin.site.register(Student,StudentAdmin)
