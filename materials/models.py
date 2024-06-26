from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """ Модель курса """
    title = models.CharField(max_length=250, verbose_name='название курса')
    description = models.TextField(**NULLABLE, verbose_name='описание курса')
    image = models.ImageField(
        upload_to='course_images/', **NULLABLE, verbose_name='превью курса'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE
    )

    def __str__(self):
        return f"course {self.title}"

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """ Модель урока """
    title = models.CharField(max_length=250, verbose_name='название урока')
    description = models.TextField(**NULLABLE, verbose_name='описание урокаа')
    image = models.ImageField(
        upload_to='course_images/', **NULLABLE, verbose_name='превью урока'
    )
    video_link = models.URLField(**NULLABLE, verbose_name='ссылка на видео')
    course = models.ForeignKey(
        Course, **NULLABLE, on_delete=models.SET_NULL, verbose_name='название курса'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE
    )

    def __str__(self):
        return f"lesson {self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    """ Модель подписки пользователя на курс """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь'
    )
    course = models.ForeignKey(
        Course, **NULLABLE, on_delete=models.SET_NULL, verbose_name='курс'
    )

    def __str__(self):
        return f"Подписка {self.user} на {self.course}"

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
