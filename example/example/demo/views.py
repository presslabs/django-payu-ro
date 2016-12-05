from payu.forms import PayULiveUpdateForm

from django.shortcuts import render


def home(request):
    order = [
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
    details = {
        'ORDER_REF': '789456123',
        'ORDER_DATE': '2016-10-05 11:12:27',
        'PRICES_CURRENCY': 'RON',
        'ORDER_SHIPPING': '0',
        'DISCOUNT': '55',
        'PAY_METHOD': 'CCVISAMC',
        'DESTINATION_CITY': 'Bucuresti',
        'DESTINATION_STATE': 'Bucuresti',
        'DESTINATION_COUNTRY': 'RO',
        'TESTORDER': 'TRUE',
        'BACK_REF': 'http://localhost:8000/',
        'BILL_FNAME': 'Joe',
        'BILL_LNAME': 'Doe',
        'BILL_COUNTRYCODE': 'RO',
        'BILL_PHONE': '+040000000000',
        'BILL_EMAIL': 'joe.doe@gmail.com',
    }

    payu_dict = details.copy()
    payu_dict['ORDER'] = order

    payu_form = PayULiveUpdateForm(initial=payu_dict)

    return render(request, 'simple_payment.html', {
        'form': payu_form,
        'orders': order,
        'details': details,
        'order_hash': payu_form.fields['ORDER_HASH'].initial
    })
