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
