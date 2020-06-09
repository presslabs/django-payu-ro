# coding=utf-8
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
from django.conf import settings


PAYU_MERCHANT = getattr(settings, 'PAYU_MERCHANT', '')
PAYU_MERCHANT_KEY = getattr(settings, 'PAYU_KEY', '')
PAYU_TEST_TRANSACTION = getattr(settings, 'PAYU_TEST', 'TRUE')
PAYU_LU_CALLBACK = getattr(settings, 'PAYU_LU_CALLBACK', '')


PAYU_LU_URL = getattr(settings, 'PAYU_LU_URL',
                      'https://secure.payu.ro/order/lu.php')
PAYU_ALU_URL = getattr(settings, 'PAYU_ALU_URL',
                       'https://secure.payu.ro/order/alu/v3')
PAYU_IDN_URL = getattr(settings, 'PAYU_IDN_URL',
                       'https://secure.payu.ro/order/idn.php')

PAYU_TOKENS_URL = getattr(settings, 'PAYU_TOKENS_URL',
                          'https://secure.payu.ro/order/tokens/')

PAYU_ORDER_DETAILS = ['PNAME', 'PGROUP', 'PCODE', 'PINFO', 'PRICE', 'PRICE_TYPE',
                      'QTY', 'VAT', 'VER']

PAYU_ORDER_DETAILS_DEFAULTS = {
    'QTY': 1,
    'VAT': 24
}

PAYU_DATE_FORMATS = (
    '%Y-%m-%d %H:%M:%S'
)

PAYU_CURRENCIES = (
    ('USD', 'USD'),
    ('RON', 'RON'),
    ('EUR', 'EUR')
)

PAYU_PAYMENT_METHODS = (
    ('CCVISAMC', 'VISA/Mastercard Card'),
    ('CCAMEX', 'AMEX Card'),
    ('CCDINERS', 'Diners Club Card'),
    ('CCJCB', 'JCB Card'),
    ('WIRE', 'Bank Wire'),
    ('PAYPAL', 'PayPal')
)

PAYU_LANGUAGES = (
    ('RO', u'Română'),
    ('EN', u'English'),
    ('DE', u'Deutsch'),
    ('ES', u'Español'),
    ('FR', u'Français'),
    ('IT', u'Italiano')
)

PAYU_PAYMENT_STATUS = (
    ('PAYMENT_AUTHORIZED', 'PAYMENT_AUTHORIZED'),
    ('PAYMENT_RECEIVED', 'PAYMENT_RECEIVED'),
    ('TEST', 'TEST'),
    ('CASH', 'CASH'),
    ('COMPLETE', 'COMPLETE'),
    ('REVERSED', 'REVERSED'),
    ('REFUND', 'REFUND')
)

PAYU_IPN_FIELDS = ['SALEDATE', 'PAYMENTDATE', 'REFNO', 'REFNOEXT', 'ORDERNO',
                   'ORDERSTATUS', 'PAYMETHOD', 'PAYMETHOD_CODE', 'FIRSTNAME',
                   'LASTNAME', 'IDENTITY_NO', 'IDENTITY_ISSUER', 'CARD_TYPE',
                   'IDENTITY_CNP', 'COMPANY', 'REGISTRATIONNUMBER',
                   'FISCALCODE', 'CBANKNAME', 'CBANKACCOUNT', 'ADDRESS1',
                   'ADDRESS2', 'CITY', 'STATE', 'ZIPCODE', 'COUNTRY',
                   'COUNTRY_CODE', 'PHONE', 'FAX', 'CUSTOMEREMAIL',
                   'FIRSTNAME_D', 'LASTNAME_D', 'COMPANY_D', 'ADDRESS1_D',
                   'ADDRESS2_D', 'CITY_D', 'STATE_D', 'ZIPCODE_D', 'COUNTRY_D',
                   'COUNTRY_D_CODE', 'PHONE_D', 'EMAIL_D', 'IPADDRESS',
                   'IPCOUNTRY', 'COMPLETE_DATE', 'CURRENCY', 'LANGUAGE',
                   'IPN_PID[]', 'IPN_PNAME[]', 'IPN_PCODE[]', 'IPN_INFO[]',
                   'IPN_QTY[]', 'IPN_PRICE[]', 'IPN_VAT[]', 'IPN_VER[]',
                   'IPN_DISCOUNT[]', 'IPN_PROMONAME[]', 'IPN_PROMOCODE[]',
                   'IPN_ORDER_COSTS[]', 'IPN_REC_CURRENT_ITERATION_NO[]',
                   'IPN_REC_ORIGINAL_REFNO[]', 'IPN_REC_INTERVAL[]',
                   'IPN_REC_EXPIRATION_DATE[]', 'IPN_REC_MULTIPLIER[]',
                   'IPN_DELIVEREDCODES[]', 'IPN_DOWNLOAD_LINK', 'IPN_TOTAL[]',
                   'IPN_TOTALGENERAL', 'IPN_SHIPPING', 'IPN_REFERRER',
                   'IPN_GLOBALDISCOUNT', 'IPN_COMMISSION', 'IPN_DATE',
                   'IPN_CC_TOKEN', 'IPN_CC_MASK', 'IPN_CC_EXP_DATE', 'TOKEN_HASH']
