import hmac
from datetime import datetime

import requests

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
        parameters = "".join(["%s%s" % (len(str(parameter[1])), parameter[1])
                              for parameter in sorted_payload])
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
        payload['SIGN'] = TokenPayment.get_signature(payload, self.merchant_key)

        return payload


class ALUPayment(BasePayment):
    def pay(self):
        order = self.order

        order["MERCHANT"] = self.merchant
        order = self._build_order(order, self.token)
        order["ORDER_HASH"] = ALUPayment.get_signature(order, self.merchant_key)

        return requests.post(PAYU_ALU_URL, data=order)

    def _build_order(self, order, alu_token):
        final_order = self._parse_orders(order.pop('ORDER'))
        final_order['CC_TOKEN'] = alu_token.IPN_CC_TOKEN
        final_order.update(**order)

        return final_order

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
