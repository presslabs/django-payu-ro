#
# Copyright 2012-2016 PressLabs SRL
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

import hmac
import hashlib
from datetime import datetime

import pytz

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from payu.conf import MERCHANT_KEY
from payu.models import PayUIPN, Token
from payu.forms import PayUIPNForm


@require_POST
@csrf_exempt
def ipn(request):
    ipn_obj = None
    error = None
    ipn_form = PayUIPNForm(request.POST)

    validation_hash = "".join(['%s%s' % (len(field), field)
                               for field in request.POST.values()
                               if field != 'HASH'
                              ])
    expected_hash = hmac.new(MERCHANT_KEY, validation_hash, hashlib.md5).hexdigest()
    request_hash = request.POST.get('HASH', '')

    if request_hash != expected_hash:
        error = 'Invalid hash %s. Hash string \n%s' % (request_hash, validation_hash)
    else:
        if ipn.is_valid():
            try:
                ipn_obj = ipn.save(commit=False)
            except Exception, exception:
                error = "Exception while processing. (%s)" % exception
        else:
            error = "Invalid form. (%s)" % ipn.errors

    if not ipn_obj:
        ipn_obj = PayUIPN()

    # Set query params and sender's IP address
    ipn_obj.initialize(request)

    if error:
        # We save errors in the error field
        ipn_obj.set_flag(error)

    ipn_obj.save()
    ipn_obj.send_signals()

    # Check for a token in the request and save it if found
    IPN_CC_TOKEN = request.POST.get('IPN_CC_TOKEN')
    IPN_CC_MASK = request.POST.get('IPN_CC_MASK')
    IPN_CC_EXP_DATE = request.POST.get('IPN_CC_EXP_DATE')

    if all([IPN_CC_TOKEN, IPN_CC_MASK, IPN_CC_EXP_DATE]):
        Token.objects.create(
            IPN_CC_TOKEN=IPN_CC_TOKEN,
            IPN_CC_MASK=IPN_CC_MASK,
            IPN_CC_EXP_DATE=IPN_CC_EXP_DATE,
            ipn=ipn_obj
        ).send_signals()

    # Send confirmation to PayU that we received this request
    date = datetime.now(pytz.UTC).strftime('%Y%m%d%H%M%S')
    confirmation_hash = hmac.new(MERCHANT_KEY, '00014%s' % date).hexdigest()
    return HttpResponse('<EPAYMENT>%s|%s</EPAYMENT>' % (date, confirmation_hash))
