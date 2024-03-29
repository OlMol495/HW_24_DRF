from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """Устанавливает роли пользователей"""
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Имейл')
    phone = models.CharField(max_length=25, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    """Модель отдельного платежа, привязанного к студенту и цели оплаты"""

    CASH = "Наличные"
    BANK = "Перевод"

    PAYMENT_METHOD_CHOISE = [
        (CASH, "Наличные"),
        (BANK, "Перевод")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    payment_date = models.DateField(**NULLABLE, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='оплаченный_курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, related_name='оплаченный_урок', **NULLABLE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='сумма платежа')
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOISE, verbose_name='способ_оплаты',
                                      max_length=10, **NULLABLE)

    def __str__(self):
        return f"{self.user}: {self.course if self.course else self.lesson} - {self.payment_date}"

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('-payment_date',)