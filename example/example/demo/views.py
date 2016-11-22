from random import randint

from payu.forms import PayULiveUpdateForm

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    payment_reference = randint(500, 1000)
    price = 100
    vat = 24

    payu_dict = {
        'ORDER_REF': payment_reference,
        'ORDER': [
            {
                'PNAME': 'ACME Inc Payment',
                'PCODE': '%d' % payment_reference,
                'PRICE': price,
                'PRICE_TYPE': 'GROSS',
                'VAT': vat
            },
        ],
        'PAY_METHOD': 'CCVISAMC',
        'BACK_REF': 'http://localhost:8000/',
        'AUTOMODE': '1',
        'BILL_FNAME': 'John',
        'BILL_LNAME': 'Dow',
        'BILL_COUNTRYCODE': 'US',
        'BILL_PHONE': '+040000000000',
        'BILL_EMAIL': 'john@doe.com',
        'BILL_COMPANY': 'ACME Inc',
        'BILL_FISCALCODE': None
    }

    return render(request, 'simple_payment.html', {
        'form': PayULiveUpdateForm(initial=payu_dict)
    })
