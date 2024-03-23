from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer, UserProfileSerializer, UserPublicProfileSerializer
from rest_framework.filters import OrderingFilter


class UserViewSet(viewsets.ModelViewSet):
    """ Вывод данных по юзерам с кастомизированной вьюшкой на детали юзера """
    queryset = User.objects.all()
    default_serializer = UserSerializer  # Дефолтный сериалайзер
    serializers = {
        'retrieve': UserProfileSerializer  # Детали юзера выводятся по UserProfileSerializer
    }

    def get_serializer_class(self):
        """ Return appropriate serializer """
        if self.action == 'retrieve':
            if self.request.user == self.get_object():
                return UserProfileSerializer
            return UserPublicProfileSerializer
        return self.default_serializer


class PaymentListAPIView(generics.ListAPIView):
    """ Сериалайзер для списка платежей """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Опция фильтрации и сортировки
    filterset_fields = ('course', 'lesson', 'payment_method',)  # Поля для фильтрации
    ordering_fields = ('payment_date',)  # Поля для сортировки
    permission_classes = [IsAuthenticated]
