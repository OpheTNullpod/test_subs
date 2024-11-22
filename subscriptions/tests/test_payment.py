from django.test import TestCase
from django.contrib.auth import get_user_model
from subscriptions.models.plan import Plan
from subscriptions.models.subscription import Subscription
from subscriptions.models.payment import Payment

class PaymentModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password")
        self.plan = Plan.objects.create(name="Premium Plan", price=20.00, duration_in_days=30)
        self.subscription = Subscription.objects.create(user=self.user, plan=self.plan)
        self.payment = Payment.objects.create(
            user=self.user,
            subscription=self.subscription,
            amount=19.99,  # Corrected amount
            payment_method="stripe",
            status="pending",
            transaction_reference="txn_test_123",
        )

    def test_payment_creation(self):
        self.assertEqual(self.payment.user, self.user)
        self.assertEqual(self.payment.subscription, self.subscription)
        self.assertEqual(self.payment.amount, 19.99)
        self.assertEqual(self.payment.payment_method, 'stripe')
        self.assertEqual(self.payment.status, 'pending')

    def test_payment_status_update(self):
        self.payment.status = 'successful'
        self.payment.save()
        self.assertEqual(self.payment.status, 'successful')

    def test_payment_str(self):
        expected_str = f"Payment txn_test_123 - pending"
        self.assertEqual(str(self.payment), expected_str)
z