from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson
from users.models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class PaymentSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    lesson = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all())
    #user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField()

    def get_payments(self, user):
       return PaymentSerializer(Payment.objects.filter(user=user), many=True).data


    class Meta:
        model = User
        fields = ['email', 'phone', 'city', 'avatar', 'payments']