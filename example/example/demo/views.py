from payu.forms import PayULiveUpdateForm

from django.shortcuts import render


def home(request):
    payu_dict = {
        'LU_ENBLE_TOKEN': '1',
        'ORDER_REF': '789456123',
        'ORDER_DATE': '2016-10-05 11:12:27',
        'ORDER': [
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
            },
        ],
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

    return render(request, 'simple_payment.html', {
        'form': PayULiveUpdateForm(initial=payu_dict)
    })
