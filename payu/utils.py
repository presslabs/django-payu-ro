import hmac
from collections import OrderedDict
from xml.etree import ElementTree

import requests

from payu.conf import PAYU_IOS_URL, PAYU_MERCHANT, PAYU_MERCHANT_KEY


class PayUIOS(object):
    @classmethod
    def signature(cls, payload, merchant_key):
        confirmation_hash = "".join(["%s%s" % (len(str(payload[field])),
                                               payload[field])
                                     for field in payload])
        return hmac.new(merchant_key, confirmation_hash).hexdigest()

    @classmethod
    def _build_payload(cls, merchant, merchant_key, ref_no_ext):
        payload = OrderedDict([
            ('MERCHANT', merchant),
            ('REFNOEXT', ref_no_ext)
        ])
        payload["HASH"] = cls.signature(payload, merchant_key)

        return payload

    @classmethod
    def get_instant_order_status(cls, ipn):
        """
        :param ipn: A PayUIPN object containing the REFNOEXT attribute.
        :return: A dict containing details about the status of the order.
        """
        payload = cls._build_payload(PAYU_MERCHANT, PAYU_MERCHANT_KEY, ipn.REFNOEXT)

        response = requests.post(PAYU_IOS_URL, data=payload)

        try:
            parsed_response = ElementTree.fromstring(response.content)
        except ElementTree.ParseError:
            return {'error': "Couldn't parse the XML result from PayU.",
                    'result': response.content}

        if parsed_response.tag == 'Error':
            return {'error': parsed_response.text.strip()}

        return {child.tag: (child.text or '').strip() for child in parsed_response}
