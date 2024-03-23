from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.paginators import ListPaginator
from materials.permissions import IsModerator, IsOwner
from materials.serializers.course import CourseSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Вьюшка для модели курса"""
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    default_serializer = CourseSerializer
    serializers = {
        'retrieve': CourseDetailSerializer
    }
    pagination_class = ListPaginator

    def get_serializer_class(self):
        """Переопределение сериализатора на просмотр деталей курса"""
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        """Определяет допуски по по разным действиям CRUD"""
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """Привязывает юзера к создаваемому им курсу"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()



