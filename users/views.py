from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer, UserProfileSerializer
from rest_framework.filters import OrderingFilter


class UserViewSet(viewsets.ModelViewSet):
    """Вывод данных по юзерам с кастомизированной вьюшкой на детали юзера"""
    queryset = User.objects.all()
    default_serializer = UserSerializer #Дофолтный сериалайзер
    serializers = {
        'retrieve': UserProfileSerializer  #Детали юзера выводятся по UserProfileSerializer
    }

    def get_serializer_class(self):
        """Return appropriate serializer"""
        return self.serializers.get(self.action, self.default_serializer)

class PaymentListAPIView(generics.ListAPIView):
    """Сериалайзер для списка платежей"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter] #Опция фильтрации и сортировки
    filterset_fields = ('course', 'lesson', 'payment_method',) #Поля для фильтрации
    ordering_fields = ('payment_date',) #Поля для сортировки


class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def get_object(self):
        user = super().get_object()
        user.payments = user.payment_set.all()
        return user