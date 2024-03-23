from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson
from materials.validators import ValidateVideoLink


class LessonSerializer(serializers.ModelSerializer):
    """ Базовый сериализатор для урока """
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            ValidateVideoLink(field='video_link')
        ]


class LessonListSerializer(serializers.ModelSerializer):
    """ Сериализатор для списка уроков с указанием названия курса, к которому они относятся """
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    class Meta:
        model = Lesson
        fields = ('title', 'course',) #вывод ограничен названием урока и курсом


class LessonDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для деталей урока с указанием названия курса, к которому он относятся """
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    class Meta:
        model = Lesson
        fields = '__all__'