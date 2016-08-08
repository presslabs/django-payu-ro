# 
# Copyright 2012-2013 PressLabs SRL
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
import pytz
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from payu.conf import MERCHANT_KEY
from payu.models import PayUIPN, Token
from payu.forms import PayUIPNForm


@require_POST
@csrf_exempt
def ipn(request):
    ipn = PayUIPNForm(request.POST)
    ipn_obj = None
    flag = None

    s = ''
    for key, val in request.POST.iteritems():
        if val == 'HASH':
            continue
        s += '%s%s' % (len(val), val)

    expected_hash = hmac.new(MERCHANT_KEY, s, hashlib.md5).hexdigest()
    request_hash = request.POST.get('HASH', '')

    if request_hash != expected_hash:
        flag = 'Invalid hash %s. Hash string \n%s' % (request_hash, s)
    else:
        if ipn.is_valid():
            try:
                # When commit = False, object is returned without saving to DB.
                ipn_obj = ipn.save(commit=False)
            except Exception, e:
                flag = "Exception while processing. (%s)" % e
        else:
            flag = "Invalid form. (%s)" % ipn.errors

    if ipn_obj is None:
        ipn_obj = PayUIPN()

    # Set query params and sender's IP address
    ipn_obj.initialize(request)

    if flag is not None:
        # We save errors in the flag field
        ipn_obj.set_flag(flag)

    ipn_obj.save()
    ipn_obj.send_signals()

    # Check for a token in the request and save it if found
    IPN_CC_TOKEN = request.POST.get('IPN_CC_TOKEN')
    IPN_CC_MASK = request.POST.get('IPN_CC_MASK')
    IPN_CC_EXP_DATE = request.POST.get('IPN_CC_EXP_DATE')

    if None not in [IPN_CC_TOKEN, IPN_CC_MASK, IPN_CC_EXP_DATE]:
        token = Token.objects.create(
            IPN_CC_TOKEN=IPN_CC_TOKEN,
            IPN_CC_MASK=IPN_CC_MASK,
            IPN_CC_EXP_DATE=IPN_CC_EXP_DATE,
            ipn=ipn_obj
        )
        token.send_signals()

    # Send confirmation to PayU that we received this request
    date = datetime.now(pytz.UTC).strftime('%Y%m%d%H%M%S')
    hash = hmac.new(MERCHANT_KEY,'00014%s' % date).hexdigest()
    return HttpResponse('<EPAYMENT>%s|%s</EPAYMENT>' % (date, hash))
