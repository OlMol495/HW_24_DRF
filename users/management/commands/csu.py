from django.conf import settings
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=settings.ROOT_EMAIL,
            first_name='Admin',
            last_name='Pro',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(settings.ROOT_PASSWORD)
        user.save()