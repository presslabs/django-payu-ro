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

from datetime import datetime

import pytest
import django
from django.http import QueryDict

from payu.forms import (PayULiveUpdateForm, ValueHiddenInput, OrderWidget,
                        PayUIPNForm)


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
    }, '5b118e083e52a24872f579134c5db6cc'),
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
        'TESTORDER': 'TRUE',
        'PAY_METHOD': 'CCVISAMC'
    }, 'e327589caadf200996521a4d0b433ef5'),
    ({
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
        'BILL_FNAME': 'Joe',
        'BILL_LNAME': 'Doe',
        'BILL_COUNTRYCODE': 'RO',
        'BILL_PHONE': '+040000000000',
        'BILL_EMAIL': 'joe.doe@gmail.com',
    }, 'a9b838e17a04cc045699e5501f8f12c6')
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


@pytest.mark.parametrize("version,field,html", [
    ('', ValueHiddenInput().render('name', None), ''),

    ('1.11',
     ValueHiddenInput().render('name', ''),
     '<input type="hidden" name="name" />'),
    ('1.11',
     ValueHiddenInput().render('name', 'value'),
     '<input type="hidden" name="name" value="value" />'),
    ('1.11',
     ValueHiddenInput().render('ORDER_10_0', 'a'),
     '<input type="hidden" name="ORDER_PNAME[]" value="a" />'),
    ('1.11',
     ValueHiddenInput().render('ORDER_10_10', 'a'),
     '<input type="hidden" name="ORDER_10_10" value="a" />'),

    ('1.8',
     ValueHiddenInput().render('name', ''),
     '<input name="name" type="hidden" />'),
    ('1.8',
     ValueHiddenInput().render('name', 'value'),
     '<input name="name" type="hidden" value="value" />'),
    ('1.8',
     ValueHiddenInput().render('ORDER_10_0', 'a'),
     '<input name="ORDER_PNAME[]" type="hidden" value="a" />'),
    ('1.8',
     ValueHiddenInput().render('ORDER_10_10', 'a'),
     '<input name="ORDER_10_10" type="hidden" value="a" />'),
])
def test_value_input_hidden(version, field, html):
    if version and version not in '.'.join(map(str, django.VERSION)):
        return
    assert field == html


@pytest.mark.parametrize("decompressed_value,expected_value", [
    (OrderWidget().decompress({'n': 'test', 'm': 20}),
     ['', '', '', '', '', '', '', '', '']),
    (OrderWidget().decompress({'PNAME': 'test', 'VAT': 20}),
     ['test', '', '', '', '', '', '', 20, '']),
    (OrderWidget().decompress({'PNAME': '1', 'VAT': 20, 'PGROUP': '2',
                               'PCODE': '3', 'PINFO': '4', 'PRICE': '5'}),
     ['1', '2', '3', '4', '5', '', '', 20, ''])
])
def test_decompress_order_widget(decompressed_value, expected_value):
    assert decompressed_value == expected_value


@pytest.mark.parametrize("form_data,expected", [
    ({}, lambda form: not form.is_valid()),
    ({'REFNO': 1}, lambda form: not form.is_valid()),
    ({'REFNO': 1, 'REFNOEXT': 1}, lambda form: not form.is_valid()),
    ({'REFNO': 1, 'REFNOEXT': 1, 'ORDERNO': 1, 'ORDERSTATUS': 'TEST',
      'HASH': 'aaa', 'PAYMETHOD_CODE': 'CCVMAC'}, lambda form: form.is_valid()),
])
def test_payu_model_form_validation(form_data, expected):
    assert expected(PayUIPNForm(form_data))


def test_payu_model_form_date_conversion():
    form = PayUIPNForm({'IPN_DATE': '20161220170852'})
    assert form['IPN_DATE'].value() == datetime.strptime('20161220170852',
                                                         '%Y%m%d%H%M%S')


@pytest.mark.parametrize("form_data,expected", [
    (QueryDict('IPN_PID[]=1&IPN_PID[]=2&IPN_PID[]=3'), '1,2,3'),
    (QueryDict('IPN_PID=1'), '1'),
    (QueryDict('IPN_PID[]=1'), '1'),
    (QueryDict('IPN_PID[]='), ''),
    (QueryDict('IPN_PID[=1'), None)
])
def test_payu_model_form_list_processing(form_data, expected):
    form = PayUIPNForm(form_data)
    assert form['IPN_PID'].value() == expected
