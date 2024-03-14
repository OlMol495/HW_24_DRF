from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson
from users.models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class PaymentSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all()) #Отображение название курса
    lesson = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all()) #Отображение названия урока
    #user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField() #Отображение дополнительного поля с платежами

    def get_payments(self, user):
        """передача в платежи всех данных из сериалайзера платежей"""
        return PaymentSerializer(Payment.objects.filter(user=user), many=True).data


    class Meta:
        model = User
        fields = ['email', 'phone', 'city', 'avatar', 'payments']

    # def to_representation(self, instance):
    #     """Modify the output data format based on the current user."""
    #     ret = super().to_representation(instance)
    #     # Check if the current user is viewing their own profile
    #     if self.context['request'].user != instance:
    #         # If not, remove sensitive information
    #         ret.pop('payments', None)
    #
    #     return ret


class UserPublicProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'phone', 'city', 'avatar']
