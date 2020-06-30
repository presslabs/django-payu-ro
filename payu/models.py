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
import hmac
from datetime import datetime
from collections import OrderedDict

import pytz
import requests

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.six import text_type

from payu.signals import (payment_completed, payment_authorized,
                          payment_flagged, alu_token_created)
from payu.conf import (PAYU_PAYMENT_STATUS, PAYU_IDN_URL,
                       PAYU_MERCHANT, PAYU_MERCHANT_KEY)


class PayUIPN(models.Model):
    REFNO = models.CharField(max_length=9, verbose_name='ePayment reference')
    REFNOEXT = models.CharField(max_length=100, verbose_name='Merchant reference')
    ORDERNO = models.CharField(max_length=6, verbose_name='Merchant order #')
    ORDERSTATUS = models.CharField(max_length=18, choices=PAYU_PAYMENT_STATUS,
                                   verbose_name='Status')
    HASH = models.CharField(max_length=64)
    PAYMETHOD_CODE = models.CharField(max_length=10,
                                      verbose_name='Payment method code')

    SALEDATE = models.DateTimeField(blank=True, null=True,
                                    verbose_name='Sale date')
    COMPLETE_DATE = models.DateTimeField(blank=True, null=True,
                                         verbose_name='Complete date')
    PAYMENTDATE = models.DateTimeField(blank=True, null=True,
                                       verbose_name='Payment date')

    PAYMETHOD = models.CharField(blank=True, null=True, max_length=100,
                                 verbose_name='Payment method')
    FIRSTNAME = models.CharField(blank=True, null=True, max_length=40,
                                 help_text='Client\'s first name')
    LASTNAME = models.CharField(blank=True, null=True, max_length=40,
                                help_text='Client\'s last name')
    IDENTITY_NO = models.CharField(blank=True, null=True, max_length=15,
                                   help_text='Customer ID Card series and \
                                   number (Series / Number - available \
                                   only for Romanian customers)')
    IDENTITY_ISSUER = models.CharField(blank=True, null=True, max_length=100,
                                       help_text='IDENTITY_NO ID Card \
                                       issuer authority ')
    CARD_TYPE = models.CharField(blank=True, null=True, max_length=100,
                                 help_text='Used credit card type. \
                                 Ex: "Visa" or "MasterCard"')
    IDENTITY_CNP = models.CharField(blank=True, null=True, max_length=13,
                                    help_text='Customer\'s personal numeric \
                                    code, available only for Romanian customers.')
    COMPANY = models.CharField(blank=True, null=True, max_length=40,
                               help_text='Company name (maximum length: \
                                             40 characters) ')
    REGISTRATIONNUMBER = models.CharField(blank=True, null=True, max_length=40,
                                          help_text='Company\'s Commerce \
                                          Registry registration number \
                                          (maximum length: 40 characters)')
    FISCALCODE = models.CharField(blank=True, null=True, max_length=40,
                                  help_text='Unique Registration Number / \
                                  VAT ID (maximum length: 40 characters)')
    CBANKNAME = models.CharField(blank=True, null=True, max_length=40,
                                 help_text='Company\'s Bank (maximum \
                                 length: 40 characters) ')
    CBANKACCOUNT = models.CharField(blank=True, null=True, max_length=50,
                                    help_text='Company\'s Bank Account \
                                    (maximum length: 50 characters)')
    ADDRESS1 = models.CharField(blank=True, null=True, max_length=100,
                                help_text='Address (maximum length: 100 \
                                characters)')
    ADDRESS2 = models.CharField(blank=True, null=True, max_length=100,
                                help_text='Additional Address info \
                                (maximum length: 100 characters)')
    CITY = models.CharField(blank=True, null=True, max_length=30,
                            help_text='City (maximum length: 30 characters)')
    STATE = models.CharField(blank=True, null=True, max_length=30,
                             help_text='State/Sector/County (maximum \
                             length: 30 characters)')
    ZIPCODE = models.CharField(blank=True, null=True, max_length=20,
                               help_text='ZIP/Postal Code (maximum length: \
                               20 characters)')
    COUNTRY = models.CharField(blank=True, null=True, max_length=50,
                               help_text='Country (maximum length: 50 \
                               characters)')
    COUNTRY_CODE = models.CharField(blank=True, null=True, max_length=10,
                                    help_text='Country (maximum length: 10 \
                                    characters)')
    PHONE = models.CharField(blank=True, null=True, max_length=40,
                             help_text='Phone number (maximum length: 40 \
                             characters)')
    FAX = models.CharField(blank=True, null=True, max_length=40,
                           help_text='Fax number (maximum length: 40 \
                           characters)')
    CUSTOMEREMAIL = models.CharField(blank=True, null=True, max_length=40,
                                     help_text='Customer\'s e-mail address \
                                     (maximum length: 40 characters)')
    FIRSTNAME_D = models.CharField(blank=True, null=True, max_length=40,
                                   help_text='First name (maximum length: \
                                   40 characters) ')
    LASTAME_D = models.CharField(blank=True, null=True, max_length=40,
                                 help_text='Last Name (maximum length: 40 \
                                 characters)')
    COMPANY_D = models.CharField(blank=True, null=True, max_length=50,
                                 help_text='Company (maximum length: 50 \
                                 characters)')
    ADDRESS1_D = models.CharField(blank=True, null=True, max_length=100,
                                  help_text='Address (maximum length: 100 \
                                  characters)')
    ADDRESS2_D = models.CharField(blank=True, null=True, max_length=100,
                                  help_text='Additional address info \
                                  (maximum length: 100 characters)')
    CITY_D = models.CharField(blank=True, null=True, max_length=30,
                              help_text='City (maximum length: 30 \
                              characters)')
    STATE_D = models.CharField(blank=True, null=True, max_length=30,
                               help_text='State/Sector/County (maximum \
                               length: 30 characters)')
    ZIPCODE_D = models.CharField(blank=True, null=True, max_length=20,
                                 help_text='ZIP/Postal Code (maximum \
                                 length: 20 characters)')
    COUNTRY_D = models.CharField(blank=True, null=True, max_length=50,
                                 help_text='Country (maximum length: 50 \
                                 characters)')
    COUNTRY_D_CODE = models.CharField(blank=True, null=True, max_length=10,
                                      help_text='Country (maximum length: \
                                      10 characters)')
    PHONE_D = models.CharField(blank=True, null=True, max_length=40,
                               help_text='Phone number (maximum length: 40 \
                               characters)')
    EMAIL_D = models.CharField(blank=True, null=True, max_length=40,
                               help_text='E-mail (maximum length: 40 \
                               characters)')
    IPADDRESS = models.CharField(blank=True, null=True, max_length=250,
                                 help_text='Client\'s IP Address (maximum \
                                 length: 250 characters)')
    IPCOUNTRY = models.CharField(blank=True, null=True, max_length=50,
                                 help_text='Client\'s IP Country (maximum \
                                 length: 50 characters)')
    COMPLETE_DATE = models.CharField(blank=True, null=True, max_length=40,
                                     help_text='The order completion date, \
                                     in the following format: Y-m-d H:i:s \
                                     (2012-04-26 15:02:28) .')
    CURRENCY = models.CharField(blank=True, null=True, max_length=10,
                                help_text='The currency in which the order \
                                has been processed. Possible values: RON, \
                                USD, EUR.')
    LANGUAGE = models.CharField(blank=True, null=True, max_length=40,
                                help_text='The language in which the order \
                                has been processed. Possible values: ro, \
                                en, fr, de, it.')

    IPN_PID = models.TextField(blank=True, null=True,
                               help_text='Array with the ID Codes of the \
                               ordered products, in the PayU database (PayU \
                               reference) ')
    IPN_PNAME = models.TextField(blank=True, null=True,
                                 help_text='Array with product names ')
    IPN_PCODE = models.TextField(blank=True, null=True,
                                 help_text='Array with the product codes \
                                 assigned by the vendor in the system (vendor \
                                 reference)')
    IPN_INFO = models.TextField(blank=True, null=True,
                                help_text='Array with additional \
                                information sent for each ordered product (if \
                                they have been sent to PayU)')
    IPN_QTY = models.TextField(blank=True, null=True,
                               help_text='Array with the product quantities')
    IPN_PRICE = models.TextField(blank=True, null=True,
                                 help_text='Array with unit prices per \
                                 product (without VAT), in RON, with \
                                 period/full-stop (.) as decimal place \
                                 separator')
    IPN_VAT = models.TextField(blank=True, null=True,
                               help_text='Array with VAT values per \
                               product, with period "." as decimal place \
                               separator')
    IPN_VER = models.TextField(blank=True, null=True,
                               help_text='Array with product versions \
                               (maximum length: 50 characters)')
    IPN_DISCOUNT = models.TextField(blank=True, null=True,
                                    help_text='Array with the amounts with \
                                    which there has been made a discount \
                                    in a promotion. Including VAT. ')
    IPN_PROMONAME = models.TextField(blank=True, null=True,
                                     help_text='Array with the names of the \
                                     promotions in which the discounts \
                                     specified above have been made.')
    IPN_PROMOCODE = models.TextField(blank=True, null=True,
                                     help_text='Array with the code of the \
                                     promotions in which the discounts \
                                     specified above have been made.')
    IPN_ORDER_COSTS = models.TextField(blank=True, null=True,
                                       help_text='Array with costs for each \
                                       product from order (expressed in \
                                       order\'s currency)')
    IPN_REC_CURRENT_ITERATION_NO = models.TextField(blank=True, null=True,
                                                    help_text='Current recurring \
                                                                  period (avaible \
                                                                  only for recurrent \
                                                                  payments)')
    IPN_REC_ORIGINAL_REFNO = models.TextField(blank=True, null=True,
                                              help_text='Array containing \
                                                            the reference to \
                                                            the original order')
    IPN_REC_INTERVAL = models.TextField(blank=True, null=True,
                                        help_text='Array containing \
                                                      recurring intervals \
                                                      (day/month/week) for \
                                                      each order')
    IPN_REC_EXPIRATION_DATE = models.TextField(blank=True, null=True,
                                               help_text='Array with \
                                                             expiration dates \
                                                             for each \
                                                             recurrence')
    IPN_REC_MULTIPLIER = models.TextField(blank=True, null=True,
                                          help_text='Array with reccurence \
                                                        period (interval x \
                                                        multiplier) for each \
                                                        product from the order')
    IPN_DELIVEREDCODES = models.TextField(blank=True, null=True,
                                          help_text='Array with the codes \
                                                        delivered to the \
                                                        clients, if the PayU \
                                                        contract contains this \
                                                        feature. Each element \
                                                        in the array is \
                                                        represented by a \
                                                        string, having comma \
                                                        (,) as a separator for \
                                                        each sent code, in \
                                                        case the ordered \
                                                        quantity is greater \
                                                        than 1.')
    IPN_DOWNLOAD_LINK = models.CharField(blank=True, null=True, max_length=250,
                                         help_text='Download link of the \
                                                       product delivered to \
                                                       the client')
    IPN_TOTAL = models.TextField(blank=True, null=True,
                                 help_text='Partial total on order line \
                                               (including VAT), with \
                                               period/full-stop (.) as a \
                                               decimal place separator')
    IPN_TOTALGENERAL = models.CharField(blank=True, null=True, max_length=40,
                                        help_text='Total transaction \
                                                      amount, including VAT \
                                                      costs, with \
                                                      period/full-stop (.) as \
                                                      a decimal place \
                                                      separator')
    IPN_SHIPPING = models.CharField(blank=True, null=True, max_length=50,
                                    help_text='Total amount paid for \
                                                  shippment')
    IPN_REFERRER = models.CharField(blank=True, null=True, max_length=250,
                                    help_text='HTTP referrer of the sale.')
    IPN_GLOBALDISCOUNT = models.CharField(blank=True, null=True, max_length=250,
                                          help_text='Global discount of the \
                                                        sale. This field is \
                                                        option and is avaible \
                                                        only if the amount is \
                                                        greater than zero.')
    IPN_COMMISSION = models.CharField(blank=True, null=True, max_length=50,
                                      help_text='Payu\'s commision in RON, \
                                                    with period/full-stop (.) \
                                                    as a decimal place \
                                                    separator.')
    IPN_DATE = models.DateTimeField(blank=True, null=True, max_length=40,
                                    help_text='IPN POST\'s sending date in the \
                                               following format: YmdHMS (ex.: \
                                               20120426145935)')

    response = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    flag = models.BooleanField(default=False)
    flag_info = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_flag(self, info):
        """
        Sets a flag on the transaction and also sets a reason.
        """

        self.flag = True
        self.flag_info += info

    @property
    def is_authorized(self):
        return self.ORDERSTATUS in ['PAYMENT_AUTHORIZED', 'PAYMENT_RECEIVED', 'TEST']

    @property
    def is_completed(self):
        return self.ORDERSTATUS == 'COMPLETE'

    def __unicode__(self):
        return u'<IPN: %s>' % self.REFNO

    class Meta:
        verbose_name = 'PayU IPN'
        db_table = 'payu_ipn'
        app_label = 'payu'


class PayUIDN(models.Model):
    ipn = models.OneToOneField(PayUIPN)
    sent = models.BooleanField(default=False)

    success = models.BooleanField(default=False)
    response = models.TextField(blank=True)

    class Meta:
        verbose_name = 'PayU IDN'
        app_label = 'payu'

    def send(self):
        payload = self._build_payload(PAYU_MERCHANT, PAYU_MERCHANT_KEY)

        try:
            response = requests.post(PAYU_IDN_URL, data=payload)

            self.success = response.status_code == 200
            self.response = response.content
        except Exception as e:
            self.response = text_type(e)
            self.success = False

        self.sent = True
        self.save()

    @classmethod
    def signature(cls, payload, merchant_key):
        confirmation_hash = text_type().join(
            [text_type('{length}{value}').format(
                    length=len(text_type(value).encode('utf-8')), value=value
            ) for value in payload.values()]
        ).encode('utf-8')
        return hmac.new(merchant_key, confirmation_hash).hexdigest()

    def _build_payload(self, merchant, merchant_key, now=None):
        payload = OrderedDict([
            ('MERCHANT', merchant),
            ('ORDER_REF', self.ipn.REFNO or -1),
            ('ORDER_AMOUNT', self.ipn.IPN_TOTALGENERAL or 0),
            ('ORDER_CURRENCY', self.ipn.CURRENCY or 'RON'),
            ('IDN_DATE', now or datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),
        ])
        payload["ORDER_HASH"] = self.signature(payload, merchant_key)

        return payload

    def __unicode__(self):
        return u'<IDN: %s>' % self.pk


class PayUToken(models.Model):
    ipn = models.OneToOneField(PayUIPN)

    # used for token/v1 api payments (same value as IPN's REFNO)
    IPN_CC_TOKEN = models.CharField(max_length=9, verbose_name="Token")

    # can be used for the `IPN_CC_TOKEN` field in alu/v3 token payments
    TOKEN_HASH = models.CharField(max_length=64, verbose_name="Token Hash", blank=True, null=True)

    # documentation is unclear of the length and format of this field
    IPN_CC_MASK = models.CharField(max_length=36, verbose_name="Last 4 digits")

    IPN_CC_EXP_DATE = models.DateField(verbose_name="Expiration date")

    class Meta:
        verbose_name = 'PayU Tokens V1'
        app_label = 'payu'

    def __unicode__(self):
        return u'<Token: %s>' % (self.TOKEN_HASH or self.IPN_CC_TOKEN)


@receiver(post_save, sender=PayUToken)
def post_payu_ipn_cc_token_save(sender, instance=None, **kwargs):
    alu_token_created.send(sender=instance)


@receiver(post_save, sender=PayUIPN)
def post_payu_ipn_save(sender, instance=None, **kwargs):
    if instance.flag:
        payment_flagged.send(sender=instance)
        return

    if instance.is_authorized:
        payment_authorized.send(sender=instance)

    if instance.is_completed:
        payment_completed.send(sender=instance)
