# -*- coding: utf-8 -*-
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

import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PayUIPN'
        db.create_table('payu_ipn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('HASH', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('SALEDATE', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('COMPLETE_DATE', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('PAYMENTDATE', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('REFNO', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('REFNOEXT', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ORDERNO', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('ORDERSTATUS', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('PAYMETHOD_CODE', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('response', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flag_info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('payu', ['PayUIPN'])


    def backwards(self, orm):
        # Deleting model 'PayUIPN'
        db.delete_table('payu_ipn')


    models = {
        'payu.payuipn': {
            'COMPLETE_DATE': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'HASH': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'Meta': {'object_name': 'PayUIPN', 'db_table': "'payu_ipn'"},
            'ORDERNO': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'ORDERSTATUS': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'PAYMENTDATE': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'PAYMETHOD_CODE': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'REFNO': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'REFNOEXT': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'SALEDATE': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flag_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['payu']
