# coding=utf-8

#  Copyright (c) 2017 Presslabs SRL
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
import responses
from django.conf import settings
from mock import patch, MagicMock

from freezegun import freeze_time
from responses import matchers

from payu.payments import TokenPayment, ALUPayment
from payu.conf import PAYU_TOKENS_URL, PAYU_ALU_URL


@pytest.mark.parametrize(
    "order, key, signature",
    [
        (
            {
                "AMOUNT": 1,
                "CURRENCY": "RON",
                "BILL_ADDRESS": "address 1",
                "BILL_CITY": "Iasi",
                "BILL_EMAIL": "john@doe.com",
                "BILL_FNAME": "John",
                "BILL_LNAME": "Doe",
                "BILL_PHONE": "0243236298",
                "DELIVERY_ADDRESS": "address 2",
                "DELIVERY_CITY": "Suceava",
                "DELIVERY_EMAIL": "john@doe.com",
                "DELIVERY_FNAME": "John",
                "DELIVERY_LNAME": "Doe",
                "DELIVERY_PHONE": "0243236298",
                "EXTERNAL_REF": "25787sa1",
            },
            b"123",
            "c6d24967498508cbfeefa26095613716",
        ),
        (
            {
                "AMOUNT": 1,
                "CURRENCY": "RON",
                "BILL_EMAIL": "john@doe.com",
                "BILL_LNAME": "Doe",
                "DELIVERY_CITY": "Suceava",
                "DELIVERY_EMAIL": "john@doe.com",
                "EXTERNAL_REF": "25787sa1",
            },
            b"-1",
            "e3103c723372424b2b8292bbf6fcb436",
        ),
        (
            {
                "AMOUNT": 1,
                "CURRENCY": "MXN",
                "BILL_EMAIL": "juan@jose.com",
                "BILL_LNAME": "Jose",
                "DELIVERY_CITY": "Ciudad de México",
                "EXTERNAL_REF": "25787sa1",
            },
            b"-1",
            "0c79288878d66cd85c02c09664547625",
        ),
        (
            {
                "AMOUNT": 1,
            },
            b"",
            "bef91610dda7aabfe371623edb399f3e",
        ),
    ],
)
def test_payment_signature(order, key, signature):
    assert TokenPayment.get_signature(order, key) == signature
    assert ALUPayment.get_signature(order, key) == signature


@patch("payu.payments.requests")
def test_token_pay(mocked_requests):
    payment = TokenPayment("", "")
    payment._build_payload = MagicMock(return_value="expected_payload")

    expected_response = "ok"
    mocked_requests.post.return_value = MagicMock(content=expected_response)

    assert payment.pay() == expected_response
    mocked_requests.post.assert_called_once_with(
        PAYU_TOKENS_URL, data="expected_payload"
    )


@patch("payu.payments.datetime")
def test_token_build_payload(mocked_datetime):
    payment = TokenPayment({"AMOUNT": 1}, "token", b"key", "test")

    mocked_datetime.now.return_value = MagicMock(strftime=MagicMock(return_value="now"))
    assert payment._build_payload() == {
        "AMOUNT": 1,
        "MERCHANT": "test",
        "METHOD": "TOKEN_NEWSALE",
        "REF_NO": "token",
        "SIGN": "4192969bae28a16ba4777354903f895a",
        "TIMESTAMP": "now",
    }


def test_alu_token_pay():
    payment = ALUPayment(order="", token="")
    payment._build_payload = MagicMock(return_value="expected_payload")

    response = b"ok"
    responses.add(
        responses.POST,
        settings.PAYU_CALLBACK_URL,
        body=response,
        status=200,
        match=[
            lambda request: (request.body == "expected_payload", "body needs to match"),
        ],
    )

    assert payment.pay() == response


def test_alu_token_pay_authorization_declined():
    payment = ALUPayment(order="", token="")
    payment._build_payload = MagicMock(return_value="expected_payload")

    response = b"""
    <?xml version="1.0"?>
    <EPAYMENT>
        <REFNO>6468866</REFNO>
        <ALIAS></ALIAS>
        <STATUS>FAILED</STATUS>
        <RETURN_CODE>AUTHORIZATION_FAILED</RETURN_CODE>
        <RETURN_MESSAGE>Authorization declined</RETURN_MESSAGE>
        <DATE>2013-02-27 17:55:16</DATE>
        <ORDER_REF>7308</ORDER_REF>
        <AUTH_CODE>449322</AUTH_CODE>
        <HASH>b0fb097ecb973316b2740192b655f41e</HASH>
    </EPAYMENT>
    """

    responses.add(
        responses.POST,
        settings.PAYU_ALU_URL,
        body=response,
        status=200,
        match=[
            lambda request: (request.body == "expected_payload", "body needs to match"),
        ],
    )

    assert payment.pay() == response


@freeze_time("2020-06-30 11:49:52")
def test_alu_token_build_payload():
    payment = ALUPayment(
        order={
            "AMOUNT": 1,
            "ORDER": [
                {
                    "PNAME": "CD Player",
                    "PCODE": "PROD_04891",
                    "PINFO": "Extended Warranty - 5 Years",
                    "PRICE": "82.3",
                    "PRICE_TYPE": "GROSS",
                    "QTY": "7",
                    "VAT": "20",
                }
            ],
        },
        token="token",
        merchant_key=b"key",
        merchant="test",
    )

    assert payment._build_payload() == {
        "AMOUNT": 1,
        "MERCHANT": "test",
        "CC_TOKEN": "token",
        "ORDER_DATE": "2020-06-30 11:49:52",
        "ORDER_HASH": "a25afe5b6fd8246e7b8c8846535ba01b",
        "ORDER_PCODE[0]": "PROD_04891",
        "ORDER_PINFO[0]": "Extended Warranty - 5 Years",
        "ORDER_PNAME[0]": "CD Player",
        "ORDER_PRICE[0]": "82.3",
        "ORDER_PRICE_TYPE[0]": "GROSS",
        "ORDER_QTY[0]": "7",
        "ORDER_VAT[0]": "20",
    }
