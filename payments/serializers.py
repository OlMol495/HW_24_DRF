from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson
from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all()) #Отображение название курса
    lesson = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all()) #Отображение названия урока
    #user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


