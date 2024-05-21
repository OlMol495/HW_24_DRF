from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription


@shared_task
def course_update_mail(course_id):
    subscriptions = Subscription.objects.filter(course=course_id)
    for subscription in subscriptions:
        send_mail(
            subject='Обновления курса',
            message=f'Курс {subscription.course.title},'
                    f' на который вы подписаны, обновлен',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscription.user.email]
        )

# @shared_task
# def course_update_notification(course, email):
#     send_mail(
#         subject='Уведомление от сервиса обучения',
#         message=f'Курс {course} на который вы подписаны обновлен',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[email]
#         )
