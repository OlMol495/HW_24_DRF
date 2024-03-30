from django.db import models

from materials.models import Course, Lesson
from users.models import User

NULLABLE = {'blank': True, 'null': True}

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

class CoursePrice(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    price = models.IntegerField(verbose_name='цена курса')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stripe_product_id = models.CharField(max_length=100, **NULLABLE)
    stripe_price_id = models.CharField(max_length=100, **NULLABLE)

    def __str__(self) -> str:
        return f"{self.course.title} {self.price}"

    class Meta:
        verbose_name = 'Цена курса'
        verbose_name_plural = 'Цены курсов'


class LessonPrice(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок')
    price = models.IntegerField(verbose_name='цена курса')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.lesson.title} {self.price}"

    class Meta:
        verbose_name = 'Цена урока'
        verbose_name_plural = 'Цены уроков'
