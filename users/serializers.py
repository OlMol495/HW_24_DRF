from rest_framework import serializers

from payments.models import Payment
from payments.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class UserProfileSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField() #Отображение дополнительного поля с платежами

    def get_payments(self, user):
        """передача в платежи всех данных из сериалайзера платежей"""
        return PaymentSerializer(Payment.objects.filter(user=user), many=True).data


    class Meta:
        model = User
        fields = ['email', 'phone', 'city', 'avatar', 'payments']


class UserPublicProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'phone', 'city', 'avatar']
