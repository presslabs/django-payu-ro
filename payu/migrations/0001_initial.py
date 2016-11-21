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

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayUIPN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HASH', models.CharField(max_length=64)),
                ('SALEDATE', models.DateTimeField(null=True, verbose_name=b'Sale date', blank=True)),
                ('COMPLETE_DATE', models.DateTimeField(null=True, verbose_name=b'Complete date', blank=True)),
                ('PAYMENTDATE', models.DateTimeField(null=True, verbose_name=b'Payment date', blank=True)),
                ('REFNO', models.CharField(max_length=9, verbose_name=b'ePayment reference')),
                ('REFNOEXT', models.CharField(max_length=100, verbose_name=b'Merchant reference')),
                ('ORDERNO', models.CharField(max_length=6, verbose_name=b'Merchant order #')),
                ('ORDERSTATUS', models.CharField(max_length=18, verbose_name=b'Status', choices=[(b'PAYMENT_AUTHORIZED', b'PAYMENT_AUTHORIZED'), (b'PAYMENT_RECEIVED', b'PAYMENT_RECEIVED'), (b'TEST', b'TEST'), (b'CASH', b'CASH'), (b'COMPLETE', b'COMPLETE'), (b'REVERSED', b'REVERSED'), (b'REFUND', b'REFUND')])),
                ('PAYMETHOD_CODE', models.CharField(max_length=10, verbose_name=b'Payment method')),
                ('response', models.TextField(blank=True)),
                ('ip_address', models.IPAddressField(blank=True)),
                ('flag', models.BooleanField(default=False)),
                ('flag_info', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'payu_ipn',
                'verbose_name': 'PayU IPN',
            },
            bases=(models.Model,),
        ),
    ]
