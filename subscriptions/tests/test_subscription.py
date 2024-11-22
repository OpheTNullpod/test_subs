from django.test import TestCase
from django.contrib.auth import get_user_model
from subscriptions.models.subscription import Subscription
from subscriptions.models.plan import Plan
from django.utils import timezone

class SubscriptionTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password")
        self.plan = Plan.objects.create(name="Premium Plan", price=20.00, duration_in_days=30)
        self.subscription = Subscription.objects.create(user=self.user, plan=self.plan)

    def test_activate_subscription(self):
        self.subscription.activate()
        self.assertEqual(self.subscription.status, 'active')
        self.assertIsNotNone(self.subscription.start_date)
        self.assertIsNotNone(self.subscription.end_date)
        self.assertTrue(self.subscription.end_date > self.subscription.start_date)

    def test_renew_subscription(self):
        self.subscription.activate()
        old_end_date = self.subscription.end_date
        self.subscription.renew()
        self.assertEqual(self.subscription.status, 'renewing')
        self.assertTrue(self.subscription.end_date > old_end_date)

    def test_cancel_subscription(self):
        self.subscription.activate()
        self.subscription.cancel()
        self.assertEqual(self.subscription.status, 'cancelled')
        self.assertTrue(self.subscription.end_date <= timezone.now())
