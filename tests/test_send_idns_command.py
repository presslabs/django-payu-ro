import pytest
from mock import patch
from django_dynamic_fixture import G

from django.core.management import call_command

from payu.models import PayUIDN


@pytest.mark.django_db
@patch('payu.models.requests')
def test_send_idn_payu(mocked_requests):
    mocked_requests.post().status_code = 200
    mocked_requests.post().content = "ok"

    idns = [G(PayUIDN) for _ in xrange(4)]

    idns_args = [str(idn.pk) for idn in idns[:2]]
    call_command('send_idns', '--idns=%s' % ','.join(idns_args))

    for idn in idns[:2]:
        idn.refresh_from_db()

        assert idn.sent
        assert idn.success
        assert idn.response == "ok"


@pytest.mark.django_db
@patch('payu.models.requests')
def test_send_idn_payu_fail(mocked_requests):
    mocked_requests.post.side_effect = Exception("error")

    idn = G(PayUIDN)

    call_command('send_idns')

    idn.refresh_from_db()

    assert idn.sent
    assert not idn.success
    assert idn.response == "error"
