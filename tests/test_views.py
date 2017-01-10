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

from django.http import QueryDict
from django.test import Client
from django.core.urlresolvers import reverse

from payu.models import PayUIPN
from payu.views import ipn


@pytest.mark.django_db
@pytest.mark.parametrize('method, status_code', [
    ('get', 200),
    pytest.mark.xfail(("post", 403)),
    ('put', 405),
    ('patch', 405),
    ('delete', 405)
])
def test_ipn_view_methods_access(method, status_code):
    client = Client()
    assert getattr(client, method)(reverse('payu-ipn')).status_code == status_code


@pytest.mark.django_db
def test_ipn_view_valid_payload():
    post_data = {
        'HASH': '30dcbb067e28aee6cfefbf45e9285d7b',
        'REFNO': '10',
        'REFNOEXT': '1',
        'ORDERNO': '1',
        'ORDERSTATUS': 'TEST',
        'PAYMETHOD_CODE': 'CCVMC',
    }
    client = Client()

    response = client.post(reverse('payu-ipn'), post_data)
    assert 'EPAYMENT' in response.content

    ipn = PayUIPN.objects.filter(REFNO=post_data['REFNO']).first()
    assert ipn

    for field in post_data:
        assert getattr(ipn, field) == post_data[field]

    assert ipn.flag_info == ''
    assert not ipn.flag
