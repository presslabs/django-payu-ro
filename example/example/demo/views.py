from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View

from payu.alu import ALUPayment
from payu.forms import PayULiveUpdateForm
from payu.models import PayUIPN, ALUToken


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
    'ORDER_DATE': '2017-01-04 12:08:40',
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


def obtain_alu_token(request):
    details = DETAILS.copy()

    details.pop('TESTORDER')
    details['LU_ENABLE_TOKEN'] = '1'

    payu_dict = details.copy()
    payu_dict['ORDER'] = ORDER[:1]
    payu_dict['ORDER'][0]['PRICE'] = 1
    payu_dict['ORDER'][0]['QTY'] = 1

    payu_form = PayULiveUpdateForm(initial=payu_dict)

    return render(request, 'live_update_with_token.html', {
        'form': payu_form,
        'orders': ORDER,
        'details': details,
        'order_hash': payu_form.fields['ORDER_HASH'].initial
    })


def debug(request):
    print request.POST
    from pprint import pprint as pp
    pp(request.POST)


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

        alu_tokens = ALUToken.objects.filter(ipn_id__in=ipns)

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

        alu_token = ALUToken.objects.get(pk=request.POST['alu-token'])
        payment = ALUPayment(order, alu_token)

        respone = payment.pay()
        return HttpResponse(respone.content)
