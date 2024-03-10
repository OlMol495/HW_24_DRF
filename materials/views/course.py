from rest_framework import viewsets, serializers

from materials.models import Course, Lesson
from materials.serializers.course import CourseSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Вьюшка для модели курса"""
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializers = {
        'retrieve': CourseDetailSerializer
    }

    def get_serializer_class(self):
        """Переопределение сериализатора на просмотр деталей курса"""
        return self.serializers.get(self.action, self.default_serializer)





