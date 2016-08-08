# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IPN_CC_TOKEN', models.CharField(max_length=9, verbose_name=b'Token')),
                ('IPN_CC_MASK', models.CharField(max_length=36, verbose_name=b'Last 4 digits')),
                ('IPN_CC_EXP_DATE', models.DateField(verbose_name=b'Expiration date')),
                ('ipn', models.OneToOneField(to='payu.PayUIPN')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
