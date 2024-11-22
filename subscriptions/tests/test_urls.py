from django.test import SimpleTestCase
from django.urls import resolve, reverse
from subscriptions.views import (
    PlanListView, PlanDetailView,
    SubscriptionListView, SubscriptionDetailView,
    PaymentListView, PaymentDetailView,
    create_checkout_session,
)

class TestUrls(SimpleTestCase):
    """
    Tests for URL resolution in the subscriptions app.
    """
    
    def test_plan_list_url(self):
        url = reverse('plan_list')
        self.assertEqual(
            resolve(url).func.view_class, PlanListView,
            f"{url} did not resolve to PlanListView"
        )
    
    def test_plan_detail_url(self):
        url = reverse('plan_detail', args=[1])
        self.assertEqual(
            resolve(url).func.view_class, PlanDetailView,
            f"{url} did not resolve to PlanDetailView"
        )

    def test_subscription_list_url(self):
        url = reverse('subscription_list')
        self.assertEqual(
            resolve(url).func.view_class, SubscriptionListView,
            f"{url} did not resolve to SubscriptionListView"
        )
    
    def test_subscription_detail_url(self):
        url = reverse('subscription_detail', args=[1])
        self.assertEqual(
            resolve(url).func.view_class, SubscriptionDetailView,
            f"{url} did not resolve to SubscriptionDetailView"
        )
    
    def test_payment_list_url(self):
        url = reverse('payment_list')
        self.assertEqual(
            resolve(url).func.view_class, PaymentListView,
            f"{url} did not resolve to PaymentListView"
        )
    
    def test_payment_detail_url(self):
        url = reverse('payment_detail', args=[1])
        self.assertEqual(
            resolve(url).func.view_class, PaymentDetailView,
            f"{url} did not resolve to PaymentDetailView"
        )
    
    def test_create_checkout_session_url(self):
        url = reverse('create_checkout_session')
        self.assertEqual(
            resolve(url).func, create_checkout_session,
            f"{url} did not resolve to create_checkout_session"
        )
