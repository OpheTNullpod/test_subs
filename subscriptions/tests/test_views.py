import json
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth import get_user_model
from subscriptions.models.plan import Plan
from subscriptions.models.subscription import Subscription
from subscriptions.models.payment import Payment

# Stripe Integration Test

class StripeIntegrationTest(TestCase):
    @patch("stripe.checkout.Session.create")
    def test_create_checkout_session(self, mock_create):
        # Mock Stripe response
        mock_create.return_value = type("Session", (object,), {"id": "test_session_id"})()

        # Make POST request with valid payload
        response = self.client.post(
            reverse('create_checkout_session'),
            data=json.dumps({"price_id": "price_1QNsP4Aguj1wKeSvenuqLW07", "quantity": 1}),
            content_type="application/json"
        )

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check JSON response
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['id'], "test_session_id")

        # Check Stripe API call
        mock_create.assert_called_once_with(
            payment_method_types=['card'],
            line_items=[{
                'price': "price_1QNsP4Aguj1wKeSvenuqLW07",
                'quantity': 1,
            }],
            mode='subscription',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )

    def test_create_checkout_session_invalid_payload(self):
        # Ensure the payload is missing or invalid
        response = self.client.post(
            reverse('create_checkout_session'),
            data=json.dumps({"price_id": ""}),  # Missing or invalid price_id
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    @patch("stripe.checkout.Session.create")
    def test_create_checkout_session_stripe_error(self, mock_create):
        # Simulate a Stripe API error
        mock_create.side_effect = Exception("Stripe API error")
        response = self.client.post(
            reverse('create_checkout_session'),
            data=json.dumps({"price_id": "price_1QNsP4Aguj1wKeSvenuqLW07", "quantity": 1}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())



# Plan Views Test
class PlanViewTest(TestCase):
    def setUp(self):
        self.plan = Plan.objects.create(
            name="Basic Plan",
            price=10.00,
            description="Basic subscription plan",
            duration_in_days=30,
            is_active=True,
        )
    
    def test_plan_list(self):
        response = self.client.get(reverse('plan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_plan_detail(self):
        response = self.client.get(reverse('plan_detail', args=[self.plan.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Basic Plan")

# Subscription Views Test
class SubscriptionViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password")
        self.plan = Plan.objects.create(name="Premium Plan", price=20.00, duration_in_days=30)
        self.subscription = Subscription.objects.create(user=self.user, plan=self.plan)
    
    def test_subscription_list(self):
        response = self.client.get(reverse('subscription_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
    
    def test_subscription_detail(self):
        response = self.client.get(reverse('subscription_detail', args=[self.subscription.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], "inactive")

# Payment Views Test
class PaymentViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password")
        self.plan = Plan.objects.create(name="Premium Plan", price=20.00, duration_in_days=30)
        self.subscription = Subscription.objects.create(user=self.user, plan=self.plan)
        self.payment = Payment.objects.create(
            user=self.user,
            subscription=self.subscription,
            amount=self.plan.price,
            payment_method="stripe",
            status="pending",
        )
    
    def test_payment_list(self):
        response = self.client.get(reverse('payment_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
    
    def test_payment_detail(self):
        response = self.client.get(reverse('payment_detail', args=[self.payment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], "pending")
