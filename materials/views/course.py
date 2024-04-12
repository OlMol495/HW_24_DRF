
from rest_framework import viewsets, serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Course, Lesson, Subscription
from materials.paginators import ListPaginator
from materials.permissions import IsModerator, IsOwner
from materials.serializers.course import CourseSerializer, CourseDetailSerializer
from payments.models import CoursePrice
from materials.tasks import course_update_mail


class CourseViewSet(viewsets.ModelViewSet):
    """Вьюшка для модели курса"""
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    default_serializer = CourseSerializer
    serializers = {
        'retrieve': CourseDetailSerializer
    }
    pagination_class = ListPaginator

    def __init__(self, **kwargs):
        super().__init__(kwargs)


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

    def get_context_data(self, **kwargs):
        context = super().self.get_context_data()
        context["prices"] = CoursePrice.objects.filter(course=self.get_object())
        return context

    # def update(self, request, *args, **kwargs):
    #     course_id = self.kwargs.get('pk')
    #     course = get_object_or_404(Course, id=course_id)
    #
    #     for field in request.data:
    #         if hasattr(course, field):
    #             setattr(course, field, request.data.get(field))
    #
    #     course.save()
    #
    #     subscriptions = Subscription.objects.filter(course=course).select_related('user', 'course')
    #     for subscription in subscriptions:
    #         course_update_notification.delay(subscription.course.title, subscription.user.email)
    #     return Response({'message': f'курс "{course}" обновлен'}, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        course_update = serializer.save()
        course_id = self.kwargs['pk']
        course_update.save()
        course_update_mail.delay(course_id)

    # def get_serializer_context(self):
    #     # Get the original context data
    #     context = super().get_serializer_context()
    #     # Add anything else you want to include
    #     context['prices'] = CoursePrice.objects.filter(course=self.get_object())
    #     return context
