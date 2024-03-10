from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    """Заполнение таблицы Payment"""
    def handle(self, *args, **options):
        users = User.objects.all() #берем из базы список юзеров, т.к. платежи привязаны по foreignkey
        courses = Course.objects.all() #берем из базы список курсов, т.к. платежи привязаны по foreignkey
        lessons = Lesson.objects.all() #берем из базы список классов, т.к. платежи привязаны по foreignkey

        payment_list = [
            {"user": users[2], "payment_date": "2024-02-01", "course": courses[1], "amount": "60000",
             "payment_method": "перевод"},
            {"user": users[1], "payment_date": "2023-12-20", "lesson": lessons[7], "amount": "5000",
             "payment_method": "перевод"},
            {"user": users[3], "payment_date": "2023-09-01", "course": courses[2], "amount": "70000",
             "payment_method": "перевод"},
            {"user": users[3], "payment_date": "2024-02-28", "lesson": lessons[2], "amount": "6000",
             "payment_method": "наличные"},
        ]

        payments_to_add = []  #формируем список платежей для одновременной загрузки в базу
        for payment in payment_list:
            payments_to_add.append(Payment(**payment))

        Payment.objects.bulk_create(payments_to_add) #загружаем весь список платежей в базу
