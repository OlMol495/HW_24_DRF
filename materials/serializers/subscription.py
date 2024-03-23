from rest_framework import serializers

from materials.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Базовый сериализатор для подписки """
    class Meta:
        model = Subscription
        fields = '__all__'
