import logging
from datetime import datetime, timedelta

from celery import shared_task

from users.models import User


@shared_task
def deactivate_user():
    thirty_days_ago = datetime.now() - timedelta(days=30)

    inactive_users = User.objects.filter(
        last_login__lt=thirty_days_ago,
        is_staff=False,
        is_superuser=False
    )
    inactive_users.update(is_active=False)