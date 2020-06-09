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

import hmac
from datetime import datetime

import requests

from django.utils.six import text_type

from payu.conf import (PAYU_MERCHANT_KEY, PAYU_MERCHANT,
                       PAYU_ALU_URL, PAYU_TOKENS_URL)


class BasePayment(object):
    def __init__(self, order, token, merchant_key=PAYU_MERCHANT_KEY,
                 merchant=PAYU_MERCHANT):

        self.order = order
        self.token = token
        self.merchant_key = merchant_key
        self.merchant = merchant

    def pay(self):
        raise NotImplementedError

    @classmethod
    def get_signature(self, payload, merchant_key):
        sorted_payload = sorted(payload.items(), key=lambda item: item[0])
        parameters = text_type().join(
            [text_type('{length}{value}').format(
                length=len(text_type(parameter[1]).encode('utf-8')), value=parameter[1]
            ) for parameter in sorted_payload]
        ).encode('utf-8')
        return hmac.new(merchant_key, parameters).hexdigest()


class TokenPayment(BasePayment):
    def pay(self):
        return requests.post(PAYU_TOKENS_URL,
                             data=self._build_payload()).content

    def _build_payload(self):
        payload = {
            'REF_NO': self.token,
            'METHOD': 'TOKEN_NEWSALE',
            'MERCHANT': self.merchant,
            'TIMESTAMP': datetime.now().strftime("%Y%m%d%H%M%S"),
        }

        payload.update(self.order)

        payload['SIGN'] = self.get_signature(payload, self.merchant_key)

        return payload


class ALUPayment(BasePayment):
    def __init__(self, *args, **kwargs):
        self.lu_token_type = kwargs.pop("lu_token_type", None)

        super(ALUPayment, self).__init__(*args, **kwargs)

    def pay(self):
        return requests.post(PAYU_ALU_URL, data=self._build_payload()).content

    def _build_payload(self):
        order = self.order
        order["MERCHANT"] = self.merchant
        if not order.get("ORDER_DATE"):
            order["ORDER_DATE"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        payload = self._parse_orders(order.pop('ORDER'))
        payload['CC_TOKEN'] = self.token
        if self.lu_token_type and payload['CC_TOKEN']:
            payload['CC_CVV'] = ""
            payload['LU_TOKEN_TYPE'] = self.lu_token_type

        payload.update(**order)
        payload["ORDER_HASH"] = ALUPayment.get_signature(payload,
                                                         self.merchant_key)

        return payload

    def _parse_orders(self, orders):
        """
        Transform orders from list objects to PHP arrays:
            [
                {
                    'PNAME': 'CD Player',
                    'PCODE': 'PROD_04891',
                    'PINFO': 'Extended Warranty - 5 Years',
                    'PRICE': '82.3',
                    'PRICE_TYPE': 'GROSS',
                    'QTY': '7',
                    'VAT':'20'
                },
                {
                    'PNAME': 'Mobile Phone',
                    'PCODE': 'PROD_07409',
                    'PINFO': 'Dual SIM',
                    'PRICE': '1945.75',
                    'PRICE_TYPE': 'GROSS',
                    'QTY': '3',
                    'VAT':'20'
                },
                {
                    'PNAME': 'Laptop',
                    'PCODE': 'PROD_04965',
                    'PINFO': '17" Display',
                    'PRICE': '5230',
                    'PRICE_TYPE': 'GROSS',
                    'QTY': '1',
                    'VAT':'20'
                }
            ]

                ||
                \/

            {
                 'ORDER_PCODE[0]': 'PROD_04891',
                 'ORDER_PCODE[1]': 'PROD_07409',
                 'ORDER_PCODE[2]': 'PROD_04965',
                 'ORDER_PINFO[0]': 'Extended Warranty - 5 Years',
                 'ORDER_PINFO[1]': 'Dual SIM',
                 'ORDER_PINFO[2]': '17" Display',
                 'ORDER_PNAME[0]': 'CD Player',
                 'ORDER_PNAME[1]': 'Mobile Phone',
                 'ORDER_PNAME[2]': 'Laptop',
                 'ORDER_PRICE[0]': '82.3',
                 'ORDER_PRICE[1]': '1945.75',
                 'ORDER_PRICE[2]': '5230',
                 'ORDER_PRICE_TYPE[0]': 'GROSS',
                 'ORDER_PRICE_TYPE[1]': 'GROSS',
                 'ORDER_PRICE_TYPE[2]': 'GROSS',
                 'ORDER_QTY[0]': '7',
                 'ORDER_QTY[1]': '3',
                 'ORDER_QTY[2]': '1',
                 'ORDER_VAT[0]': '20',
                 'ORDER_VAT[1]': '20',
                 'ORDER_VAT[2]': '20'
            }
        """

        result = {}

        for index, order in enumerate(orders):
            for detail, value in order.iteritems():
                result["ORDER_%s[%s]" % (detail, index)] = value

        return result
