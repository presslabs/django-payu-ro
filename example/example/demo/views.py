# Copyright (c) 2017 Presslabs SRL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View

from payu.payments import ALUPayment, TokenPayment
from payu.forms import PayULiveUpdateForm
from payu.models import PayUIPN, PayUToken


ORDER = [
    {
        'PNAME': 'CD Player',
        'PCODE': 'PROD_04891',
        'PINFO': 'Extended Warranty - 5 Years',
        'PRICE': '82.3',
        'PRICE_TYPE': 'GROSS',
        'QTY': '7',
        'VAT':'20'
    },
    {
        'PNAME': 'Mobile Phone',
        'PCODE': 'PROD_07409',
        'PINFO': 'Dual SIM',
        'PRICE': '1945.75',
        'PRICE_TYPE': 'GROSS',
        'QTY': '3',
        'VAT':'20'
    },
    {
        'PNAME': 'Laptop',
        'PCODE': 'PROD_04965',
        'PINFO': '17" Display',
        'PRICE': '5230',
        'PRICE_TYPE': 'GROSS',
        'QTY': '1',
        'VAT':'20'
    }
]


DETAILS = {
    'ORDER_REF': '789456123',
    'ORDER_DATE': '2017-01-06 17:12:40',
    'PRICES_CURRENCY': 'RON',
    'CURRENCY': 'RON',
    'ORDER_SHIPPING': '0',
    'DISCOUNT': '0',
    'PAY_METHOD': 'CCVISAMC',
    'DESTINATION_CITY': 'Bucuresti',
    'DESTINATION_STATE': 'Bucuresti',
    'DESTINATION_COUNTRY': 'RO',
    'TESTORDER': 'TRUE',
    'AUTOMODE': '1',
    'BACK_REF': settings.PAYU_CALLBACK_URL,
    'BILL_FNAME': 'VLAD',
    'BILL_LNAME': 'TEMIAN',
    'BILL_COUNTRYCODE': 'RO',
    'BILL_PHONE': '+000000000000',
    'BILL_EMAIL': 'vladtemian@gmail.com',
}


def live_update(request):
    payu_dict = DETAILS.copy()
    payu_dict['ORDER'] = ORDER

    payu_form = PayULiveUpdateForm(initial=payu_dict)

    return render(request, 'live_update.html', {
        'form': payu_form,
        'orders': ORDER,
        'details': DETAILS,
        'order_hash': payu_form.fields['ORDER_HASH'].initial
    })


def obtain_ipn_token(request):
    details = DETAILS.copy()

    details.pop('TESTORDER')
    details['LU_ENABLE_TOKEN'] = '1'

    payu_dict = details.copy()
    payu_dict['ORDER'] = ORDER[:1]
    payu_dict['ORDER'][0]['PRICE'] = 1
    payu_dict['ORDER'][0]['QTY'] = 1

    payu_form = PayULiveUpdateForm(initial=payu_dict)

    return render(request, 'obtain_ipn_token.html', {
        'form': payu_form,
        'orders': ORDER,
        'details': details,
        'order_hash': payu_form.fields['ORDER_HASH'].initial
    })


def debug(request):
    from pprint import pprint as pp
    pp(request.POST)

    return HttpResponse(request.POST)


class ALUPayments(View):
    def get(self, request, *args, **kwargs):
        details = DETAILS.copy()
        details.pop('TESTORDER')

        order = details.copy()
        order['ORDER'] = ORDER[:1]
        order['ORDER'][0]['PRICE'] = 1
        order['ORDER'][0]['QTY'] = 1

        ipns = [ipn.pk for ipn in
                list(PayUIPN.objects.filter(REFNOEXT=order['ORDER_REF']))]

        alu_tokens = PayUToken.objects.filter(ipn_id__in=ipns)

        return render(request, 'choose_alu_token.html', {
            'orders': order['ORDER'],
            'details': details,
            'alu_tokens': alu_tokens
        })

    def post(self, request, *args, **kwargs):
        details = DETAILS.copy()
        details.pop('TESTORDER')

        order = details.copy()
        order['ORDER'] = ORDER[:1]
        order['ORDER'][0]['PRICE'] = 1
        order['ORDER'][0]['QTY'] = 1

        order['ORDER_TIMEOUT'] = 10 * 60
        order['ORDER_REF'] = '789456124'

        token = PayUToken.objects.get(pk=request.POST['token'])
        payment = ALUPayment(order, token.IPN_CC_TOKEN)

        respone = payment.pay()
        return HttpResponse(respone)


class TokenPayments(View):
    def get(self, request, *args, **kwargs):
        ipns = [ipn.pk for ipn in
                list(PayUIPN.objects.filter(REFNOEXT=DETAILS['ORDER_REF']))]

        tokens = PayUToken.objects.filter(ipn_id__in=ipns)

        return render(request, 'choose_token.html', {
            'initial_order_ref': DETAILS['ORDER_REF'],
            'tokens': tokens
        })

    def post(self, request, *args, **kwargs):
        token = PayUToken.objects.get(pk=request.POST['token'])

        payment = TokenPayment({
            "AMOUNT": 1,
            "CURRENCY": "RON",
            "BILL_ADDRESS": "address 1",
            "BILL_CITY": "Iasi",
            "BILL_EMAIL": "john@doe.com",
            "BILL_FNAME": "John",
            "BILL_LNAME": "Doe",
            "BILL_PHONE": "0243236298",
            "DELIVERY_ADDRESS": "address 2",
            "DELIVERY_CITY": "Suceava",
            "DELIVERY_EMAIL": "john@doe.com",
            "DELIVERY_FNAME": "John",
            "DELIVERY_LNAME": "Doe",
            "DELIVERY_PHONE": "0243236298",
            "EXTERNAL_REF": "789456123",
        }, token.IPN_CC_TOKEN)
        result = payment.pay()

        return HttpResponse(result)
