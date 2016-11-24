import pytest

from .forms import PayULiveUpdateForm, OrdersField


PAYU_PAYLOAD = {
    'ORDER_REF': 112457,
    'ORDER_DATE': '2012-05-01 15:51:35',
    'ORDER': [
        {
            'PNAME': 'MacBook Air 13 inch',
            'PCODE': 'MBA13',
            'PINFO': 'Extended Warranty - 5 Years',
            'PRICE': 1750,
            'PRICE_TYPE': 'GROSS',
            'QTY': 1,
            'VAT': 24
        },
    ],
    'BILL_FNAME': 'Joe',
    'BILL_LNAME': 'Doe',
    'BILL_COUNTRYCODE': 'RO',
    'BILL_PHONE': '+040000000000',
    'BILL_EMAIL': 'joe.doe@gmail.com',
    'BILL_COMPANY': 'ACME Inc',
    'BILL_FISCALCODE': None,
    'PRICES_CURRENCY': 'RON',
    'CURRENCY': 'RON',
    'PAY_METHOD': 'CCVISAMC'
}


@pytest.fixture
def payu_form():
    return PayULiveUpdateForm(initial=PAYU_PAYLOAD)


def test_calculate_correct_hash(payu_form):
    assert payu_form.signature == 'c6e9b0135191e9103beaf1e0f5ab6096'
    assert payu_form.fields['ORDER_HASH'].initial == 'c6e9b0135191e9103beaf1e0f5ab6096'


def test_orders_parsing(payu_form):
    expected_orders = [{
        'VER': None,
        'PRICE_TYPE': 'GROSS',
        'PRICE': 1750,
        'QTY': 1,
        'PINFO': 'Extended Warranty - 5 Years',
        'PCODE': 'MBA13',
        'PNAME': 'MacBook Air 13 inch',
        'PGROUP': None,
        'VAT': 24
    }]

    assert payu_form._prepare_orders(PAYU_PAYLOAD['ORDER']) == expected_orders
