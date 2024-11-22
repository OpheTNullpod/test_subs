from rest_framework import serializers
from .models.plan import Plan
from .models.subscription import Subscription
from .models.payment import Payment


# Serializer for the Plan model
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


# Serializer for the Subscription model
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


# Serializer for the Payment model
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
