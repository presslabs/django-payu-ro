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
import re
import hmac
from datetime import datetime

from django import forms
from django.utils.six import text_type

from payu.models import PayUIPN
from payu.conf import (PAYU_MERCHANT, PAYU_MERCHANT_KEY, PAYU_TEST_TRANSACTION,
                       PAYU_ORDER_DETAILS, PAYU_ORDER_DETAILS_DEFAULTS,
                       PAYU_DATE_FORMATS, PAYU_CURRENCIES,
                       PAYU_PAYMENT_METHODS, PAYU_LANGUAGES,
                       PAYU_LU_CALLBACK)


class ValueHiddenInput(forms.HiddenInput):
    """
    Widget that renders only if it has a value.
    Used to remove unused fields from PayU buttons.
    """

    template_name = 'custom_hidden.html'

    def _get_name(self, name):
        detail = re.match(r'^ORDER_(\d+)_(\d+)$', name)
        if detail and int(detail.group(2)) < len(PAYU_ORDER_DETAILS):
            name = 'ORDER_%s[]' % PAYU_ORDER_DETAILS[int(detail.group(2))]
        return name

    def get_context(self, name, value, attrs):
        context = super(ValueHiddenInput, self).get_context(name, value, attrs)
        context['widget']['name'] = self._get_name(context['widget']['name'])
        return context

    def render(self, name, value, attrs=None):
        if value is None:
            return text_type()

        name = self._get_name(name)

        return super(ValueHiddenInput, self).render(name, value or "", attrs)


class OrderWidget(forms.MultiWidget):
    def __init__(self, attrs={}, *args, **kwargs):
        all_widgets = [ValueHiddenInput(attrs) for _ in PAYU_ORDER_DETAILS]
        super(OrderWidget, self).__init__(all_widgets, *args, **kwargs)

    def decompress(self, value):
        return [value.get(detail, '') for detail in PAYU_ORDER_DETAILS]


class OrderField(forms.MultiValueField):
    widget = OrderWidget

    def __init__(self, *args, **kwargs):
        all_fields = tuple(forms.CharField() for _ in PAYU_ORDER_DETAILS)
        super(OrderField, self).__init__(all_fields, *args, **kwargs)


class OrdersWidget(forms.MultiWidget):
    is_hidden = True

    def __init__(self, count, *args, **kwargs):
        all_widgets = tuple((OrderWidget()) for _ in range(count))
        super(OrdersWidget, self).__init__(all_widgets, *args, **kwargs)


class OrdersField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        products = kwargs.get('initial', [])
        kwargs['label'] = ''

        all_fields = tuple()
        if products:
            self.widget = OrdersWidget(len(products))
            all_fields = tuple((OrderField()) for _ in products)
        super(OrdersField, self).__init__(all_fields, *args, **kwargs)


class PayULiveUpdateForm(forms.Form):
    MERCHANT = forms.CharField(widget=ValueHiddenInput,
                               initial=PAYU_MERCHANT)
    LU_ENABLE_TOKEN = forms.CharField(widget=ValueHiddenInput, initial='')
    LU_TOKEN_TYPE = forms.CharField(widget=ValueHiddenInput, initial='')
    ORDER_REF = forms.CharField(widget=ValueHiddenInput, initial='')
    ORDER_DATE = forms.CharField(widget=ValueHiddenInput,
                                 initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    ORDER = OrdersField()
    ORDER_SHIPPING = forms.CharField(widget=ValueHiddenInput)
    PRICES_CURRENCY = forms.ChoiceField(widget=ValueHiddenInput,
                                        choices=PAYU_CURRENCIES, initial='USD')
    DISCOUNT = forms.CharField(widget=ValueHiddenInput)

    DESTINATION_CITY = forms.CharField(widget=ValueHiddenInput)
    DESTINATION_STATE = forms.CharField(widget=ValueHiddenInput)
    DESTINATION_COUNTRY = forms.CharField(widget=ValueHiddenInput)

    PAY_METHOD = forms.ChoiceField(widget=ValueHiddenInput,
                                   choices=PAYU_PAYMENT_METHODS)

    ORDER_HASH = forms.CharField(widget=ValueHiddenInput,
                                 initial='')

    BILL_FNAME = forms.CharField(widget=ValueHiddenInput)
    BILL_LNAME = forms.CharField(widget=ValueHiddenInput)
    BILL_COUNTRYCODE = forms.CharField(widget=ValueHiddenInput)
    BILL_CITY = forms.CharField(widget=ValueHiddenInput)
    BILL_PHONE = forms.CharField(widget=ValueHiddenInput)
    BILL_EMAIL = forms.CharField(widget=ValueHiddenInput)
    BILL_COMPANY = forms.CharField(widget=ValueHiddenInput)
    BILL_FISCALCODE = forms.CharField(widget=ValueHiddenInput)

    CURRENCY = forms.ChoiceField(widget=ValueHiddenInput,
                                 choices=PAYU_CURRENCIES, initial='USD')
    AUTOMODE = forms.CharField(widget=ValueHiddenInput,
                               initial='1')
    LANGUAGE = forms.ChoiceField(widget=ValueHiddenInput,
                                 choices=PAYU_LANGUAGES, initial='EN')
    SELECTED_INSTALLMENTS_NO = forms.CharField(widget=ValueHiddenInput)
    BACK_REF = forms.CharField(widget=ValueHiddenInput,
                               initial=PAYU_LU_CALLBACK)
    TESTORDER = forms.CharField(widget=ValueHiddenInput,
                                initial=str(PAYU_TEST_TRANSACTION).upper())

    @property
    def signature(self):
        """
        Compute the ORDER_HASH of the request.

        The hashable string is composed by getting the values from:
            MERCHANT
            ORDER_REF
            ORDER_DATE
            ORDER_PNAME[]
            ORDER_PCODE[]
            ORDER_PINFO[]
            ORDER_PRICE[]
            ORDER_QTY[]
            ORDER_VAT[]
            ORDER_SHIPPING
            PRICES_CURRENCY
            DISCOUNT
            DESTINATION_CITY
            DESTINATION_STATE
            DESTINATION_COUNTRY
            PAY_METHOD
            ORDER_PRICE_TYPE[]
            SELECTED_INSTALLMENTS_NO
            TESTORDER
        in this exact order. Next, we need to concatenate their lenghts with
        thier values, resulting in a string like:

        8PAYUDEMO9789456123192016-10-05 11:12:279CD Player12MobilePhone6Laptop
        10PROD_0489110PROD_0740910PROD_0496527Extended Warranty - 5 Years8
        Dual SIM1117"Display482.371945.7545230171311220220220103RON2559
        Bucuresti9Bucuresti2RO8CCVISAMC5GROSS5GROSS5GROSS4TRUE

        Using this string and the MERCHANT_KEY, we compute the HMAC.
        """

        hashable_fields = ['MERCHANT', 'ORDER_REF', 'ORDER_DATE',
                           'ORDER_SHIPPING', 'PRICES_CURRENCY', 'DISCOUNT',
                           'DESTINATION_CITY', 'DESTINATION_STATE',
                           'DESTINATION_COUNTRY', 'PAY_METHOD',
                           'SELECTED_INSTALLMENTS_NO', 'TESTORDER']
        result = text_type()

        # We need this hack since payU is not consistent
        # with the order of fields in hash string

        suffix = text_type()
        for field in self:
            if field.name == 'ORDER_HASH':
                continue

            field_value = field.value()

            if field.name in hashable_fields and field_value:
                encoded_value = text_type('{length}{value}').format(
                    length=len(text_type(field_value).encode('utf-8')), value=field_value
                )
                if field.name == 'TESTORDER' or \
                    field.name == 'SELECTED_INSTALLMENTS_NO':
                    suffix += encoded_value
                else:
                    result += encoded_value

            if field.name == 'ORDER':
                for detail in PAYU_ORDER_DETAILS:
                    if any([detail in order and order[detail]
                            for order in field_value]):

                        for order in field_value:
                            value = order.get(detail, '')

                            item = text_type('{length}{value}').format(
                                length=len(text_type(value).encode('utf-8')), value=value
                            )

                            if detail == 'PRICE_TYPE':
                                suffix += item
                            else:
                                result += item

        result += suffix
        result = result.encode('utf-8')
        return hmac.new(PAYU_MERCHANT_KEY, result).hexdigest()

    def _prepare_orders(self, orders):
        """
        Each order needs to have all it's details filled with default value,
        or None, in case those are not already filled.
        """

        for detail in PAYU_ORDER_DETAILS:
            if not any([detail in order for order in orders]):
                for order in orders:
                    order[detail] = PAYU_ORDER_DETAILS_DEFAULTS.get(detail, None)

        return orders

    def __init__(self, **kwargs):
        initial = kwargs.get('initial', {})
        orders = self._prepare_orders(initial.get('ORDER', []))

        super(PayULiveUpdateForm, self).__init__(**kwargs)

        self.fields['ORDER'] = OrdersField(initial=orders)
        self.fields['ORDER_HASH'].initial = self.signature


class PayUIPNForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = PayUIPN

    def __init__(self, data, *args, **kwargs):
        form_data = data.copy()

        for field in data:
            if field.endswith("[]"):
                form_data[field[:-2]] = ",".join([value
                                                  for value in data.getlist(field)
                                                  if value.strip()
                                                 ])

            if field == 'IPN_DATE':
                form_data[field] = datetime.strptime(data[field], "%Y%m%d%H%M%S")

        super(PayUIPNForm, self).__init__(form_data)
