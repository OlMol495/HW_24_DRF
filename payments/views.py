from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from .models import Payment, CoursePrice
from .serializers import PaymentSerializer
import stripe
from django.conf import settings

from .services import StripeService


class PaymentListAPIView(generics.ListAPIView):
    """ Сериалайзер для списка платежей """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Опция фильтрации и сортировки
    filterset_fields = ('course', 'lesson', 'payment_method',)  # Поля для фильтрации
    ordering_fields = ('payment_date',)  # Поля для сортировки
    permission_classes = [IsAuthenticated]


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(APIView):
    """
    Создает сессию оплаты и перенаправляет пользователя на страничку оплаты Stripe
    """

    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('pk')
        course = Course.objects.get(id=course_id)
        course_price = CoursePrice.objects.get(course=course)
        stripe_api = StripeService()
        price = stripe_api.create_product(course.title, course_price.price)
        course_price.stripe_price_id = price['id']
        course_price.stripe_product_id = price['product']
        course_price.save()
        base_url = f'{self.request.scheme}://{self.request.get_host()}'
        session = stripe_api.create_session(course_price.stripe_price_id, base_url, course_id)

        return Response({'session': session.url})
