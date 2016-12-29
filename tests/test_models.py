import pytest
from mock import patch

from payu.models import PayUIPN, PayUPaymentToken


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


@patch('payu.models.payment_authorized')
def test_payu_model_authorized_signals(mock_authorized):
    model = PayUIPN(ORDERSTATUS='TEST')
    model.send_signals()

    mock_authorized.send.assert_called_once_with(sender=model)


@patch('payu.models.payment_completed')
def test_payu_model_completed_signals(mock_completed):
    model = PayUIPN(ORDERSTATUS='COMPLETE')
    model.send_signals()

    mock_completed.send.assert_called_once_with(sender=model)


@patch('payu.models.payment_flagged')
def test_payu_model_flagged_signals(mock_flagged):
    model = PayUIPN(flag=True)
    model.send_signals()

    mock_flagged.send.assert_called_once_with(sender=model)


@pytest.mark.parametrize('merchant, data, expected_signature', [
    ('a', {'timestamp': '1'},
     '24ce92ab6d6eb0cc16caad0a5c0123740d4645555557b6a61d1fd161348156a9'),
    ('a', {'timestamp': '2'},
     '022ec70a44137fbd56dae03b025c61c8e7752909a3d7cf5c79af785860720df5'),
    ('a', {'timestamp': '2', 'refNo': '1'},
     '1192defee8401749b2ff2d8e531fc46af04d5e0661bdd7f117f8281b7084bd58'),
])
def test_payu_payment_token(merchant, data, expected_signature):
    assert PayUPaymentToken.signature(merchant, **data) == expected_signature
