#
# Copyright 2012-2016 PressLabs SRL
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

from django.db import models

from payu.signals import (payment_completed, payment_authorized,
                          payment_flagged, token_created)
from payu.conf import PAYU_PAYMENT_STATUS


class PayUIPN(models.Model):
    HASH = models.CharField(max_length=64)
    SALEDATE = models.DateTimeField(blank=True, null=True,
                                    verbose_name='Sale date')
    COMPLETE_DATE = models.DateTimeField(blank=True, null=True,
                                         verbose_name='Complete date')
    PAYMENTDATE = models.DateTimeField(blank=True, null=True,
                                       verbose_name='Payment date')
    REFNO = models.CharField(max_length=9, verbose_name='ePayment reference')
    REFNOEXT = models.CharField(max_length=100, verbose_name='Merchant reference')
    ORDERNO = models.CharField(max_length=6, verbose_name='Merchant order #')
    ORDERSTATUS = models.CharField(max_length=18, choices=PAYU_PAYMENT_STATUS,
                                   verbose_name='Status')
    PAYMETHOD_CODE = models.CharField(max_length=10, verbose_name='Payment method')

    response = models.TextField(blank=True)
    ip_address = models.IPAddressField(blank=True)

    flag = models.BooleanField(default=False)
    flag_info = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def initialize(self, request):
        self.response = getattr(request, request.method).urlencode()
        self.ip_address = request.META.get('REMOTE_ADDR', '')

    def set_flag(self, info):
        """Sets a flag on the transaction and also sets a reason."""

        self.flag = True
        self.flag_info += info

    def send_signals(self):
        if self.flag:
            payment_flagged.send(sender=self)
            return

        if self.ORDERSTATUS in ['PAYMENT_AUTHORIZED', 'PAYMENT_RECEIVED', 'TEST']:
            payment_authorized.send(sender=self)

        if self.ORDERSTATUS == 'COMPLETE':
            payment_completed.send(sender=self)

    def __unicode__(self):
        return u'<IPN: %s>' % self.REFNO

    class Meta:
        verbose_name = 'PayU IPN'
        db_table = 'payu_ipn'


class Token(models.Model):
    ipn = models.OneToOneField(PayUIPN)

    # same value as IPN's REFNO
    IPN_CC_TOKEN = models.CharField(max_length=9, verbose_name="Token")

    # documentation is unclear of the length and format of this field
    IPN_CC_MASK = models.CharField(max_length=36, verbose_name="Last 4 digits")

    IPN_CC_EXP_DATE = models.DateField(verbose_name="Expiration date")

    def send_signals(self):
        token_created.send(sender=self)

    def __unicode__(self):
        return u'<Token: %s>' % self.IPN_CC_TOKEN
