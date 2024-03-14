from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.permissions import IsModerator, IsOwner
from materials.serializers.lesson import LessonSerializer, LessonListSerializer, LessonDetailSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """вьюшка на созданиеание урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]  # доступ имеют авторизованные пользователи, но не модер

    def perform_create(self, serializer):
        """Привязывает юзера к создаваемому им уроку"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListCreateAPIView):
    """вьюшка на просмотр списка уроков"""
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """вьюшка на просмотр конкретного урока"""
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """вьюшка на редактирование урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """вьюшка на удаление урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]  # доступ имеют авторизованные пользователи, но не модер
