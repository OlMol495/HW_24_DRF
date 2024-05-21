from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.serializers.lesson import LessonSerializer
from payments.models import CoursePrice


class CourseSerializer(serializers.ModelSerializer):
    """ Базовый сериализатор для курса """

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для просмотра деталей курса """
    lesson_count = serializers.SerializerMethodField()  # количество уроков в курсе
    lessons = LessonSerializer(source='lesson_set', many=True)
    subscription = serializers.SerializerMethodField()

    # prices = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, course):
        """ Вычисление количества уроков в курсе """
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, instance):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(
                user=user, course=instance).exists()
        return False

    # def get_prices(self, instance):
    #     prices = CoursePrice.objects.filter(course=instance)
    #     return prices
