from django.contrib import admin
from .models import Student, Subject, Exam

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Student_Code', 'Last_Name', 'First_Name', 'Course', 'Faculty', 'Group', 'Is_Headman')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('Subject_Code', 'Name', 'Hours_Per_Semester', 'Number_of_Semesters')

class ExamAdmin(admin.ModelAdmin):
    list_display = ('Exam_Code', 'Exam_Date', 'Student_Code', 'Subject_Code', 'Obtained_Grade')

admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Exam, ExamAdmin)
