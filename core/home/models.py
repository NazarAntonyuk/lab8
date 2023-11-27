from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
class Student(models.Model):
    Student_Code = models.AutoField(primary_key=True)
    Last_Name = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Patronymic = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=255)
    Course = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
    Faculty = models.CharField(max_length=255)
    Group = models.IntegerField()
    Is_Headman = models.CharField(max_length=255)

class Subject(models.Model):
    Subject_Code = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Hours_Per_Semester = models.IntegerField()
    Number_of_Semesters = models.IntegerField()

class Exam(models.Model):
    Exam_Code = models.AutoField(primary_key=True)
    Exam_Date = models.DateField()
    Student_Code = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject_Code = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Obtained_Grade = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(5)])
