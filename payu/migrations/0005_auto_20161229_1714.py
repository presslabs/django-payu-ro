# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0004_auto_20161220_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPNToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IPN_CC_TOKEN', models.CharField(max_length=9, verbose_name=b'Token')),
                ('IPN_CC_MASK', models.CharField(max_length=36, verbose_name=b'Last 4 digits')),
                ('IPN_CC_EXP_DATE', models.DateField(verbose_name=b'Expiration date')),
            ],
        ),
        migrations.CreateModel(
            name='PayUPaymentToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=40)),
                ('status', models.BooleanField(default=True)),
                ('expiration_date', models.DateTimeField(null=True, blank=True)),
                ('card_number_mask', models.CharField(max_length=40, null=True, blank=True)),
                ('card_expiration_date', models.DateTimeField(null=True, blank=True)),
                ('card_holder_name', models.CharField(max_length=40, null=True, blank=True)),
                ('card_type', models.CharField(max_length=10, null=True, blank=True)),
                ('card_bank', models.CharField(max_length=40, null=True, blank=True)),
                ('card_program_name', models.CharField(max_length=40, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='token',
            name='ipn',
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DATE',
            field=models.DateTimeField(help_text=b"IPN POST's sending date in the                                                following format: YmdHMS (ex.:                                                20120426145935)", max_length=40, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Token',
        ),
        migrations.AddField(
            model_name='ipntoken',
            name='ipn',
            field=models.OneToOneField(to='payu.PayUIPN'),
        ),
    ]
