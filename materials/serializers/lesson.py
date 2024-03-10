from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """базовый сериализатор для урока"""
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    """сериализатор для списка уроков с указанием названия курса, к которому они относятся"""
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    class Meta:
        model = Lesson
        fields = ('title', 'course',) #вывод ограничен названием урока и курсом


class LessonDetailSerializer(serializers.ModelSerializer):
    """сериализатор для деталей урока с указанием названия курса, к которому он относятся"""
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    class Meta:
        model = Lesson
        fields = '__all__'