# coding=utf-8
from django.contrib import admin
from payu.models import PayUIPN

class PayUIPNAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',
                    'REFNOEXT',
                    'ORDERSTATUS',
                    'flag',
                    'flag_info',
                    'created_at',
    )
    list_filter = ('ORDERSTATUS','flag')

admin.site.register(PayUIPN,PayUIPNAdmin)
