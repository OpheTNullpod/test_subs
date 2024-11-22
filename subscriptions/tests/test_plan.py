from django.test import TestCase
from subscriptions.models.plan import Plan

class PlanTest(TestCase):
    def setUp(self):
        self.plan = Plan.objects.create(name="Basic Plan", price=10.00, duration_in_days=30)

    def test_plan_str(self):
        self.assertEqual(str(self.plan), "Basic Plan")
        
    def test_plan_creation(self):
        self.assertEqual(self.plan.name, "Basic Plan")
        self.assertEqual(self.plan.price, 10.00)
        self.assertEqual(self.plan.duration_in_days, 30)
        self.assertTrue(self.plan.is_active)
