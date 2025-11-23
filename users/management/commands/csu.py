from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@admin.net",
            first_name="Admin",
            last_name="Adminov",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.set_password("1234")
        user.save()
        print(f"Для входа используйте admin@admin.net 1234")
