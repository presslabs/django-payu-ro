# coding=utf-8
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
from django.contrib import admin

from payu.models import PayUIPN, PayUToken, PayUIDN


class PayUIPNAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'REFNOEXT', 'ORDERSTATUS', 'flag',
                    'flag_info', 'created_at')
    list_filter = ('ORDERSTATUS', 'flag')


class PayUTokenAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'ipn', 'IPN_CC_TOKEN', 'IPN_CC_MASK',
                    'IPN_CC_EXP_DATE')


class PayUIDNAdmin(admin.ModelAdmin):
    list_display = ('ipn', 'sent', 'success')


admin.site.register(PayUIPN, PayUIPNAdmin)
admin.site.register(PayUToken, PayUTokenAdmin)
admin.site.register(PayUIDN, PayUIDNAdmin)
