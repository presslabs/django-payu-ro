# coding=utf-8
from django.conf import settings

TEST = getattr(settings, "PAYU_TEST", True)


MERCHANT = settings.PAYU_MERCHANT
MERCHANT_KEY = settings.PAYU_KEY
