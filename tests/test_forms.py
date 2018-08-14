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
                'PRICE': 1750, 'PRICE_TYPE': 'GROSS',
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


@pytest.mark.parametrize("field,html", [
    (ValueHiddenInput().render('name', None), ''),

    (ValueHiddenInput().render('name', ''), ''),
    (ValueHiddenInput().render('name', 'value'),
     '<input type="hidden" name="name" value="value" />'),
    (ValueHiddenInput().render('ORDER_10_0', 'a'),
     '<input type="hidden" name="ORDER_PNAME[]" value="a" />'),
    (ValueHiddenInput().render('ORDER_10_10', 'a'),
     '<input type="hidden" name="ORDER_10_10" value="a" />'),
])
def test_value_input_hidden(field, html):
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


@pytest.mark.parametrize("payload, html", [
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
     }, '''
<input type="hidden" name="MERCHANT" value="PAYUDEMO" id="id_MERCHANT" /><input type="hidden" name="ORDER_REF" value="112457" id="id_ORDER_REF" /><input type="hidden" name="ORDER_DATE" value="2012-05-01 15:51:35" id="id_ORDER_DATE" /><input type="hidden" name="ORDER_PNAME[]" value="MacBook Air 13 inch" id="id_ORDER_0_0" /><input type="hidden" name="ORDER_PCODE[]" value="MBA13" id="id_ORDER_0_2" /><input type="hidden" name="ORDER_PINFO[]" value="Extended Warranty - 5 Years" id="id_ORDER_0_3" /><input type="hidden" name="ORDER_PRICE[]" value="1750" id="id_ORDER_0_4" /><input type="hidden" name="ORDER_PRICE_TYPE[]" value="GROSS" id="id_ORDER_0_5" /><input type="hidden" name="ORDER_QTY[]" value="1" id="id_ORDER_0_6" /><input type="hidden" name="ORDER_VAT[]" value="24" id="id_ORDER_0_7" /><input type="hidden" name="PRICES_CURRENCY" value="RON" id="id_PRICES_CURRENCY" /><input type="hidden" name="PAY_METHOD" value="CCVISAMC" id="id_PAY_METHOD" /><input type="hidden" name="ORDER_HASH" value="5b118e083e52a24872f579134c5db6cc" id="id_ORDER_HASH" /><input type="hidden" name="BILL_FNAME" value="Joe" id="id_BILL_FNAME" /><input type="hidden" name="BILL_LNAME" value="Doe" id="id_BILL_LNAME" /><input type="hidden" name="BILL_COUNTRYCODE" value="RO" id="id_BILL_COUNTRYCODE" /><input type="hidden" name="BILL_PHONE" value="+040000000000" id="id_BILL_PHONE" /><input type="hidden" name="BILL_EMAIL" value="joe.doe@gmail.com" id="id_BILL_EMAIL" /><input type="hidden" name="BILL_COMPANY" value="ACME Inc" id="id_BILL_COMPANY" /><input type="hidden" name="CURRENCY" value="RON" id="id_CURRENCY" /><input type="hidden" name="AUTOMODE" value="1" id="id_AUTOMODE" /><input type="hidden" name="LANGUAGE" value="EN" id="id_LANGUAGE" /><input type="hidden" name="TESTORDER" value="TRUE" id="id_TESTORDER" />
     ''')
])
def test_html_rendering(payload, html):
    payu_form = PayULiveUpdateForm(initial=payload)
    assert "".join(payu_form.as_p().split("\n")) == html.split("\n")[1]
