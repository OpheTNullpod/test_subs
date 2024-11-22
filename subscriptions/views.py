from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models.plan import Plan
from .models.subscription import Subscription
from .models.payment import Payment
from .serializers import PlanSerializer, SubscriptionSerializer, PaymentSerializer
from django.views.decorators.csrf import csrf_exempt

import stripe
import json
from django.conf import settings
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

# Plan Views
class PlanListView(ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# Subscription Views
class SubscriptionListView(ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

# Payment Views
class PaymentListView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# Stripe Integration
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    try:
        # Parse JSON payload
        data = json.loads(request.body)

        # Log incoming request data
        logger.debug(f"Received data for checkout session: {data}")

        # Create Stripe session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': data['price_id'],
                'quantity': data['quantity'],
            }],
            mode='subscription',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )

        # Log successful session creation
        logger.debug(f"Stripe session created successfully: {session}")

        return JsonResponse({'id': session.id})
    except Exception as e:
        # Log error details
        logger.error(f"Error creating Stripe checkout session: {str(e)}")
        return JsonResponse({'error': str(e)}, status=400)

