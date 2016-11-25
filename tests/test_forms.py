import pytest

from payu.forms import PayULiveUpdateForm, ValueHiddenInput


@pytest.mark.parametrize("payload,signature", [
    ({
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
    }, 'c6e9b0135191e9103beaf1e0f5ab6096'),
    ({
        'ORDER_REF': 112457,
        'ORDER_DATE': '2012-05-01 15:51:35',
        'ORDER': [
            {
                'PNAME': 'MacBook Air 13 inch',
                'PCODE': 'MBA13',
                'PINFO': '',
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
        'LANGUAGE': 'RO',
        'TEST': True,
        'PAY_METHOD': 'CCVISAMC'
    }, '8d6acdf75aa76eb5da0fe6fdefd04723')
])
def test_calculate_correct_hash(payload, signature):
    payu_form = PayULiveUpdateForm(initial=payload)
    assert payu_form.signature == signature
    assert payu_form.fields['ORDER_HASH'].initial == signature


@pytest.mark.parametrize("payload,orders", [
    ({
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
    }, [{
        'VER': None,
        'PRICE_TYPE': 'GROSS',
        'PRICE': 1750,
        'QTY': 1,
        'PINFO': 'Extended Warranty - 5 Years',
        'PCODE': 'MBA13',
        'PNAME': 'MacBook Air 13 inch',
        'PGROUP': None,
        'VAT': 24
    }]),
    ({
        'ORDER': [
            {
                'PNAME': 'MacBook Air 13 inch',
                'PCODE': 'MBA13',
                'PRICE': 1750,
                'PRICE_TYPE': 'GROSS',
            },
        ],
    }, [{
        'VER': None,
        'PRICE_TYPE': 'GROSS',
        'PRICE': 1750,
        'QTY': 1,
        'PINFO': None,
        'PCODE': 'MBA13',
        'PNAME': 'MacBook Air 13 inch',
        'PGROUP': None,
        'VAT': 24
    }])
])
def test_orders_parsing(payload, orders):
    payu_form = PayULiveUpdateForm(initial=payload)
    assert payu_form._prepare_orders(payload['ORDER']) == orders


@pytest.mark.parametrize("field,html", [
    (ValueHiddenInput().render('name', None), ''),
    (ValueHiddenInput().render('name', ''), '<input name="name" type="hidden" />'),
    (ValueHiddenInput().render('name', 'value'), '<input name="name" type="hidden" value="value" />'),
    (ValueHiddenInput().render('ORDER_10_0', 'a'), '<input name="ORDER_PNAME[]" type="hidden" value="a" />'),
    (ValueHiddenInput().render('ORDER_10_10', 'a'), '<input name="ORDER_10_10" type="hidden" value="a" />'),
])
def test_value_input_hiddend(field, html):
    assert field == html
