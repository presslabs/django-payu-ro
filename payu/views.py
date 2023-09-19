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

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from payu.conf import PAYU_MERCHANT_KEY, PAYU_IPN_FIELDS
from payu.models import PayUIPN, PayUToken, PayUIDN
from payu.forms import PayUIPNForm


@csrf_exempt
@require_http_methods(["POST", "GET"])
def ipn(request):
    if request.method == "GET":
        return HttpResponse()

    ipn_obj = None
    error = None

    form_data = request.POST
    ipn_form = PayUIPNForm(form_data)

    validation_hash = ""
    for field in PAYU_IPN_FIELDS:
        if field not in request.POST:
            continue

        field_value = request.POST.getlist(field)

        validation_hash += "".join(
            [
                "{length}{value}".format(length=len(value.encode("utf-8")), value=value)
                for value in field_value
            ]
        )

    validation_hash = validation_hash.encode("utf-8")

    expected_hash = hmac.new(
        PAYU_MERCHANT_KEY, validation_hash, hashlib.md5
    ).hexdigest()
    request_hash = request.POST.get("HASH", "")

    if request_hash != expected_hash:
        error = "Invalid hash %s. Hash string \n%s" % (request_hash, expected_hash)
    else:
        if ipn_form.is_valid():
            try:
                ipn_obj = ipn_form.save(commit=False)
            except Exception as exception:
                error = "Exception while processing. (%s)" % exception
        else:
            error = "Invalid form. (%s)" % ipn_form.errors

    if not ipn_obj:
        ipn_obj = PayUIPN()

    # Set query params and sender's IP address
    ipn_obj.response = getattr(request, request.method).urlencode()
    ipn_obj.ip_address = request.META.get("REMOTE_ADDR", "")

    if error:
        # We save errors in the error field
        ipn_obj.set_flag(error)

    ipn_obj.save()

    # Check for a token in the request and save it if found
    IPN_CC_TOKEN = request.POST.get("IPN_CC_TOKEN")
    TOKEN_HASH = request.POST.get("TOKEN_HASH")
    IPN_CC_MASK = request.POST.get("IPN_CC_MASK")
    IPN_CC_EXP_DATE = request.POST.get("IPN_CC_EXP_DATE")

    if all([(IPN_CC_TOKEN or TOKEN_HASH), IPN_CC_MASK, IPN_CC_EXP_DATE]):
        PayUToken.objects.create(
            IPN_CC_TOKEN=IPN_CC_TOKEN,
            IPN_CC_MASK=IPN_CC_MASK,
            IPN_CC_EXP_DATE=IPN_CC_EXP_DATE,
            TOKEN_HASH=TOKEN_HASH,
            ipn=ipn_obj,
        )

    PayUIDN.objects.create(ipn=ipn_obj)

    # Send confirmation to PayU that we received this request
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")

    confirmation_hash = b""
    for field in ["IPN_PID[]", "IPN_PNAME[]", "IPN_DATE"]:
        field_value = request.POST.getlist(field)

        if not field_value:
            confirmation_hash += b"0"
        else:
            confirmation_hash += field_value

    confirmation_hash = hmac.new(
        PAYU_MERCHANT_KEY,
        b"%s14%s" % (confirmation_hash, date.encode("utf-8")),
        hashlib.md5,
    ).hexdigest()
    return HttpResponse("<EPAYMENT>%s|%s</EPAYMENT>" % (date, confirmation_hash))
