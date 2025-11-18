from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {
                "last_name": "Абрикосов",
                "first_name": "Иван",
            },
            {
                "last_name": "Борисов",
                "first_name": "Никита",
            },
            {
                "last_name": "Владина",
                "first_name": "Дарья",
            },
            {
                "last_name": "Галинова",
                "first_name": "Екатерина",
            },
            {
                "last_name": "Данилова",
                "first_name": "Татьяна",
            },
            {
                "last_name": "Ежова",
                "first_name": "Анастасия",
            },
            {
                "last_name": "Жарин",
                "first_name": "Иван",
            },
        ]

        students_for_create = []

        for student_item in student_list:
            students_for_create.append(Student(**student_item))

        # пакетное добавление
        Student.objects.bulk_create(students_for_create)
        print("Добавлено:")
        print(students_for_create)
