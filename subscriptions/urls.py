from django.urls import path
from .views import (
    create_checkout_session,
    PlanListView,
    PlanDetailView,
    SubscriptionListView,
    SubscriptionDetailView,
    PaymentListView,
    PaymentDetailView,
)

urlpatterns = [
    # Stripe Integration
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),


    # Plan Endpoints
    path('plans/', PlanListView.as_view(), name='plan_list'),
    path('plans/<int:pk>/', PlanDetailView.as_view(), name='plan_detail'),

    # Subscription Endpoints
    path('subscriptions/', SubscriptionListView.as_view(), name='subscription_list'),
    path('subscriptions/<int:pk>/', SubscriptionDetailView.as_view(), name='subscription_detail'),

    # Payment Endpoints
    path('payments/', PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
]
