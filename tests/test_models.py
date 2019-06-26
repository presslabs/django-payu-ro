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

import pytest
from mock import patch, MagicMock
from django_dynamic_fixture import G

from payu.models import PayUIPN, PayUIDN
from payu.conf import PAYU_IDN_URL


@pytest.mark.parametrize('flag_info, extra_info', [
    ('', ''),
    ('1', ''),
    ('1', '1'),
])
def test_payu_model_flag(flag_info, extra_info):
    model = PayUIPN(flag_info=flag_info)
    model.set_flag(extra_info)
    assert model.flag_info == flag_info + extra_info
    assert model.flag


@pytest.mark.parametrize('order, authorized, completed', [
    ('1', False, False),
    ('TEST', True, False),
    ('PAYMENT_RECEIVED', True, False),
    ('PAYMENT_AUTHORIZED', True, False),
    ('COMPLETE', False, True),
    ('', False, False)
])
def test_payu_model_order_status(order, authorized, completed):
    model = PayUIPN(ORDERSTATUS=order)
    assert model.is_authorized == authorized
    assert model.is_completed == completed


@pytest.mark.django_db
@patch('payu.models.payment_authorized')
def test_payu_model_authorized_signals(mock_authorized):
    model = G(PayUIPN, ORDERSTATUS='TEST')
    mock_authorized.send.assert_called_once_with(sender=model)


@pytest.mark.django_db
@patch('payu.models.payment_completed')
def test_payu_model_completed_signals(mock_completed):
    model = G(PayUIPN, ORDERSTATUS='COMPLETE')
    mock_completed.send.assert_called_once_with(sender=model)


@pytest.mark.django_db
@patch('payu.models.payment_flagged')
def test_payu_model_flagged_signals(mock_flagged):
    model = G(PayUIPN, flag=True)
    mock_flagged.send.assert_called_once_with(sender=model)


@pytest.mark.parametrize('payload, merchant_key, signature', [
    (
        {}, b'0', '477f91ddbcc6839b9950045977da3530'
    ), (
        # example from payu docs (with actually wrong hash)
        # check online: source b"8MERCHANT73954142539.993USD192015-05-11 14:32:08"
        #               key b"1231234567890123"
        {'MERCHANT': 'MERCHANT', 'ORDER_REF': 3954142, 'ORDER_AMOUNT': 39.99,
         'ORDER_CURRENCY': 'USD', 'IDN_DATE': '2015-05-11 14:32:08'},
        b'1231234567890123', 'e40a3d1505cbb15e34cf35f34c784bb0'
)])
def test_idn_signature(payload, merchant_key, signature):
    assert PayUIDN.signature(payload, merchant_key) == signature


@pytest.mark.parametrize('payu_idn, merchant, merchant_key, now, expected_payload', [
    (PayUIPN(REFNO=1, IPN_TOTALGENERAL=1, CURRENCY='USD'), '123', b'1', 1,
     {
         'MERCHANT': '123',
         'ORDER_REF': 1,
         'ORDER_AMOUNT': 1,
         'ORDER_CURRENCY': 'USD',
         'IDN_DATE': 1,
         'ORDER_HASH': '5d275f182089bab5a5351613067b95dc'
     }),
    (PayUIPN(), '123', b'1', 1,
     {
         'MERCHANT': '123',
         'ORDER_REF': -1,
         'ORDER_AMOUNT': 0,
         'ORDER_CURRENCY': 'RON',
         'IDN_DATE': 1,
         'ORDER_HASH': '61ff18cdfe071679176f03664b4feb72'
     })

])
def test_idn_payload(payu_idn, merchant, merchant_key, now, expected_payload):
    idn = PayUIDN(ipn=payu_idn)
    assert dict(**idn._build_payload(merchant, merchant_key, now)) == expected_payload


@pytest.mark.django_db
@patch('payu.models.requests')
def test_payu_idn_send_success(mocked_requests):
    mocked_requests.post.return_value = MagicMock(status_code=200, content="ok")

    idn = PayUIDN(ipn=G(PayUIPN))
    idn._build_payload = MagicMock(return_value="payload")

    idn.send()

    mocked_requests.post.assert_called_once_with(PAYU_IDN_URL, data="payload")
    assert idn.sent
    assert idn.success
    assert idn.response == "ok"


@pytest.mark.django_db
@patch('payu.models.requests')
def test_payu_idn_send_fail(mocked_requests):
    mocked_requests.post.side_effect = Exception('error')

    idn = PayUIDN(ipn=G(PayUIPN))
    idn._build_payload = MagicMock(return_value="payload")

    idn.send()

    mocked_requests.post.assert_called_once_with(PAYU_IDN_URL, data="payload")
    assert idn.sent
    assert not idn.success
    assert idn.response == "error"
