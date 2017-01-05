import pytest

from payu.payments import TokenPayment, ALUPayment


@pytest.mark.parametrize('order, key, signature', [
    ({
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
        "EXTERNAL_REF": "25787sa1"
    }, "123", "c6d24967498508cbfeefa26095613716"),
    ({
        "AMOUNT": 1,
        "CURRENCY": "RON",
        "BILL_EMAIL": "john@doe.com",
        "BILL_LNAME": "Doe",
        "DELIVERY_CITY": "Suceava",
        "DELIVERY_EMAIL": "john@doe.com",
        "EXTERNAL_REF": "25787sa1"
    }, "-1", "e3103c723372424b2b8292bbf6fcb436"),
    ({
        "AMOUNT": 1,
    }, "", "bef91610dda7aabfe371623edb399f3e")
])
def test_payment_signature(order, key, signature):
    assert TokenPayment.get_signature(order, key) == signature
    assert ALUPayment.get_signature(order, key) == signature
