from django.core.management.base import BaseCommand
from home.scripts import *
from home.models import Student, Subject, Exam

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **options):
        fake_students = generate_fake_students()
        fake_subjects = generate_fake_subjects()

        Student.objects.bulk_create(fake_students)
        Subject.objects.bulk_create(fake_subjects)

        fake_exams = generate_fake_exams(fake_students, fake_subjects)
        Exam.objects.bulk_create(fake_exams)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data.'))
