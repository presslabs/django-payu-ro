from django.dispatch import Signal

# Sent when a payment is completed.
payment_completed = Signal()

# Sent when a payment is authorized (PAYMENT_AUTHORIZED or PAYMENT_RECEIVED)
payment_authorized = Signal()

payment_flagged = Signal()