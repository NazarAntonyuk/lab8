# Generated by Django 4.2.7 on 2023-11-19 11:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Student_Code', models.AutoField(primary_key=True, serialize=False)),
                ('Last_Name', models.CharField(max_length=255)),
                ('First_Name', models.CharField(max_length=255)),
                ('Patronymic', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Phone_Number', models.CharField(max_length=255)),
                ('Course', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('Faculty', models.CharField(max_length=255)),
                ('Group', models.IntegerField()),
                ('Is_Headman', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('Subject_Code', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Hours_Per_Semester', models.IntegerField()),
                ('Number_of_Semesters', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('Exam_Code', models.AutoField(primary_key=True, serialize=False)),
                ('Exam_Date', models.DateField()),
                ('Obtained_Grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(5)])),
                ('Student_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
                ('Subject_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject')),
            ],
        ),
    ]
