from rest_framework import serializers

from materials.models import Course, Lesson
from materials.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """базовый сериализатор для курса"""
    class Meta:
        model = Course
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    """сериализатор для просмотра деталей курса"""
    lesson_count = serializers.SerializerMethodField() #количество уроков в курсе
    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, course):
        """вычисление количества уроков в курсе"""
        return Lesson.objects.filter(course=course).count()