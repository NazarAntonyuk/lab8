import random
from home.models import Student, Subject, Exam
from faker import Faker
from home.midle_name import ukrainian_middle_names
from datetime import date

fake = Faker('uk_UA')
starost = ['Так', 'Ні']

def generate_fake_students():
    students = []
    for _ in range(11):
        last_name = fake.last_name()
        first_name = fake.first_name()
        middle_name = fake.random_element(ukrainian_middle_names)
        address = fake.address()
        phone = fake.phone_number()
        course = fake.random_int(min=1, max=4)
        faculty = fake.random_element(["Аграрний менеджмент", "Економіка", "Інформаційні технології"])
        group = fake.random_int(min=1, max=4)
        is_head = fake.random_element(starost)

        student = Student(
            Last_Name=last_name,
            First_Name=first_name,
            Patronymic=middle_name,
            Address=address,
            Phone_Number=phone,
            Course=course,
            Faculty=faculty,
            Group=group,
            Is_Headman=is_head
        )
        students.append(student)

    return students

def generate_fake_subjects():
    subject_data = [
        ('Захист Рослин', 60, 2),
        ('Бізнес Економіка', 45, 2),
        ('Програмуваня з Python', 30, 1),
    ]

    subjects = []
    for subject_info in subject_data:
        subject = Subject(
            Name=subject_info[0],
            Hours_Per_Semester=subject_info[1],
            Number_of_Semesters=subject_info[2]
        )
        subjects.append(subject)

    return subjects

def generate_fake_exams(students, subjects):
    exams = []
    start_date = date(2023, 11, 27)
    end_date = date(2023, 12, 30)

    for _ in range(20):
        exam_date = fake.date_between_dates(start_date, end_date)
        student = random.choice(students)
        subject = random.choice(subjects)
        grade = random.randint(2, 5)

        exam = Exam(
            Exam_Date=exam_date,
            Student_Code=student,
            Subject_Code=subject,
            Obtained_Grade=grade
        )
        exams.append(exam)

    return exams

