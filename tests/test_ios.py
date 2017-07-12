from collections import OrderedDict

import pytest
from mock import MagicMock, patch
from django_dynamic_fixture import G

from payu.models import PayUIPN
from payu.utils import PayUIOS


def test_ios_signature():
    # this data is taken from the PayU documentation

    payload = OrderedDict([
        ('MERCHANT', 'PAYUDEMO'),
        ('REFNOEXT', 'EPAY10425')
    ])

    signature = PayUIOS.signature(payload, merchant_key='1231234567890123')

    assert signature == '6cb19f366fd9709b078b593b1736a4ea'


def test_ios_payload():
    # this data is taken from the PayU documentation

    payload = PayUIOS._build_payload(merchant='PAYUDEMO',
                                     ref_no_ext='EPAY10425',
                                     merchant_key='1231234567890123')

    assert payload == OrderedDict([
        ('MERCHANT', 'PAYUDEMO'),
        ('REFNOEXT', 'EPAY10425'),
        ('HASH', '6cb19f366fd9709b078b593b1736a4ea')
    ])


@pytest.mark.django_db
@patch('payu.utils.requests')
def test_ios_get_instant_order_status(mocked_requests):
    response_content = """<?xml version="1.0"?>
                            <Order>
                                <ORDER_DATE>2017-07-12 12:16:20</ORDER_DATE>
                                <REFNO>45459240</REFNO>
                                <REFNOEXT>b3045b90-d11f-4c78-9f6b-79f54317df36</REFNOEXT>
                                <ORDER_STATUS>TEST</ORDER_STATUS>
                                <PAYMETHOD>Visa/MasterCard/Eurocard</PAYMETHOD>
                                <HASH>adc135ddd73f0f4fe3eb9d26b84c662d</HASH>
                            </Order>"""

    mocked_requests.post.return_value = MagicMock(status_code=200, content=response_content)

    ipn = G(PayUIPN)

    status = PayUIOS.get_instant_order_status(ipn)

    assert status == {'HASH': 'adc135ddd73f0f4fe3eb9d26b84c662d',
                      'PAYMETHOD': 'Visa/MasterCard/Eurocard',
                      'REFNO': '45459240',
                      'ORDER_STATUS': 'TEST',
                      'ORDER_DATE': '2017-07-12 12:16:20',
                      'REFNOEXT': 'b3045b90-d11f-4c78-9f6b-79f54317df36'}


@pytest.mark.django_db
@pytest.mark.parametrize('payu_response, expected_result', [
    ('<?xml version="1.0"?><Error>Limit calls for IOS exceeded!</Error>',
     {'error': 'Limit calls for IOS exceeded!'}),
    ('Access not permitted', {'error': "Couldn't parse the XML result from PayU.",
                              'result': 'Access not permitted'}),
])
@patch('payu.utils.requests')
def test_ios_get_instant_order_status_error(mocked_requests, payu_response, expected_result):
    mocked_requests.post.return_value = MagicMock(status_code=200, content=payu_response)

    ipn = G(PayUIPN)

    result = PayUIOS.get_instant_order_status(ipn)

    assert result == expected_result
