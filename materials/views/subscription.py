from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Subscription
from materials.serializers.subscription import SubscriptionSerializer


class SubscriptionAPIView(APIView):
    """вьюшка на создание и удаление подписки"""

    permission_classes = [IsAuthenticated]  # доступ имеют авторизованные пользователи

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        sub_item = Subscription.objects.filter(user=user, course=course_item)

        if sub_item.exists():
            message = 'Ваша подписка удалена'
            sub_item.delete()
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Вы подписались на курс'

        return Response({"message": message})
