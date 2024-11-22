from celery import shared_task
from .models import Payment

@shared_task
def retry_failed_payment(payment_id):
    """Retries a failed payment."""
    try:
        payment = Payment.objects.get(id=payment_id)
        if payment.status == 'failed':
            # Retry logic for the payment (example: Stripe retry implementation)
            payment.process_payment()
    except Payment.DoesNotExist:
        pass
