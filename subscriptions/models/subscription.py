from django.conf import settings
from django.db import models
from django_fsm import FSMField, transition
from django.utils import timezone
from .plan import Plan

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = FSMField(default='inactive', choices=[
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('renewing', 'Renewing'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    ])
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_recurring = models.BooleanField(default=False)

    @transition(field=status, source='inactive', target='active')
    def activate(self):
        self.start_date = timezone.now()
        self.end_date = self.start_date + timezone.timedelta(days=self.plan.duration_in_days)
        self.save()

    @transition(field=status, source='active', target='renewing')
    def renew(self):
        self.end_date = timezone.now() + timezone.timedelta(days=self.plan.duration_in_days)
        self.save()

    @transition(field=status, source=['active', 'renewing'], target='cancelled')
    def cancel(self):
        self.end_date = timezone.now()
        self.save()
