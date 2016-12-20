# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='payuipn',
            name='ADDRESS1',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Address (maximum length: 100                                 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='ADDRESS1_D',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Address (maximum length: 100                                   characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='ADDRESS2',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Additional Address info                                 (maximum length: 100 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='ADDRESS2_D',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Additional address info                                   (maximum length: 100 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='CARD_TYPE',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Used credit card type.                                  Ex: "Visa" or "MasterCard"', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='CBANKACCOUNT',
            field=models.CharField(max_length=50, null=True, verbose_name=b"Company's Bank Account                                     (maximum length: 50 characters)", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='CBANKNAME',
            field=models.CharField(max_length=40, null=True, verbose_name=b"Company's Bank (maximum                                  length: 40 characters) ", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='CITY',
            field=models.CharField(max_length=30, null=True, verbose_name=b'City (maximum length: 30 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='CITY_D',
            field=models.CharField(max_length=30, null=True, verbose_name=b'City (maximum length: 30                               characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='COMPANY',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Company name (maximum length:                                              40 characters) ', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='COMPANY_D',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Company (maximum length: 50                                  characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='COUNTRY',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Country (maximum length: 50                                characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='COUNTRY_CODE',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Country (maximum length: 10                                     characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='COUNTRY_D',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Country (maximum length: 50                                  characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='COUNTRY_D_CODE',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Country (maximum length:                                       10 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='CURRENCY',
            field=models.CharField(max_length=10, null=True, verbose_name=b'The currency in which the order                                 has been processed. Possible values: RON,                                 USD, EUR.', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='CUSTOMEREMAIL',
            field=models.CharField(max_length=40, null=True, verbose_name=b"Customer's e-mail address                                      (maximum length: 40 characters)", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='EMAIL_D',
            field=models.CharField(max_length=40, null=True, verbose_name=b'E-mail (maximum length: 40                                characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='FAX',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Fax number (maximum length: 40                            characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='FIRSTNAME',
            field=models.CharField(max_length=40, null=True, verbose_name=b"Client's first name", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='FIRSTNAME_D',
            field=models.CharField(max_length=40, null=True, verbose_name=b'First name (maximum length:                                    40 characters) ', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='FISCALCODE',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Unique Registration Number /                                   VAT ID (maximum length: 40 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IDENTITY_CNP',
            field=models.CharField(max_length=13, null=True, verbose_name=b"Customer's personal numeric                                     code, available only for Romanian customers.", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IDENTITY_ISSUER',
            field=models.CharField(max_length=100, null=True, verbose_name=b'IDENTITY_NO ID Card                                        issuer authority ', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IDENTITY_NO',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Customer ID Card series and                                    number (Series / Number - available                                    only for Romanian customers)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPADDRESS',
            field=models.CharField(max_length=250, null=True, verbose_name=b"Client's IP Address (maximum                                  length: 250 characters)", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPCOUNTRY',
            field=models.CharField(max_length=50, null=True, verbose_name=b"Client's IP Country (maximum                                  length: 50 characters)", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_COMMISSION',
            field=models.CharField(max_length=50, null=True, verbose_name=b"Payu's commision in RON,                                                     with period/full-stop (.)                                                     as a decimal place                                                     separator.", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_DATE',
            field=models.CharField(max_length=40, null=True, verbose_name=b"IPN POST's sending date in the                                               following format: YmdHis (ex.:                                               20120426145935)", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_DELIVEREDCODES',
            field=models.TextField(null=True, verbose_name=b'Array with the codes                                                         delivered to the                                                         clients, if the PayU                                                         contract contains this                                                         feature. Each element                                                         in the array is                                                         represented by a                                                         string, having comma                                                         (,) as a separator for                                                         each sent code, in                                                         case the ordered                                                         quantity is greater                                                         than 1.', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_DISCOUNT',
            field=models.TextField(null=True, verbose_name=b'Array with the amounts with                                     which there has been made a discount                                     in a promotion. Including VAT. ', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_DOWNLOAD_LINK',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Download link of the                                                        product delivered to                                                        the client', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_GLOBALDISCOUNT',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Global discount of the                                                         sale. This field is                                                         option and is avaible                                                         only if the amount is                                                         greater than zero.', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_INFO',
            field=models.TextField(null=True, verbose_name=b'Array with additional                                 information sent for each ordered product (if                                 they have been sent to PayU)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_ORDER_COSTS',
            field=models.TextField(null=True, verbose_name=b"Array with costs for each                                        product from order (expressed in                                        order's currency)", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_PCODE',
            field=models.TextField(null=True, verbose_name=b'Array with the product codes                                  assigned by the vendor in the system (vendor                                  reference)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_PID',
            field=models.TextField(null=True, verbose_name=b'Array with the ID Codes of the                                ordered products, in the PayU database (PayU                                reference) ', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_PNAME',
            field=models.TextField(null=True, verbose_name=b'Array with product names ', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_PRICE',
            field=models.TextField(null=True, verbose_name=b'Array with unit prices per                                  product (without VAT), in RON, with                                  period/full-stop (.) as decimal place                                  separator', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_PROMOCODE',
            field=models.TextField(null=True, verbose_name=b'Array with the code of the                                      promotions in which the discounts                                      specified above have been made.', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_PROMONAME',
            field=models.TextField(null=True, verbose_name=b'Array with the names of the                                      promotions in which the discounts                                      specified above have been made.', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_QTY',
            field=models.TextField(null=True, verbose_name=b'Array with the product quantities', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_REC_CURRENT_ITERATION_NO',
            field=models.TextField(null=True, verbose_name=b'Current recurring                                                                   period (avaible                                                                   only for recurrent                                                                   payments)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_REC_EXPIRATION_DATE',
            field=models.TextField(null=True, verbose_name=b'Array with                                                              expiration dates                                                              for each                                                              recurrence', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_REC_INTERVAL',
            field=models.TextField(null=True, verbose_name=b'Array containing                                                       recurring intervals                                                       (day/month/week) for                                                       each order', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_REC_MULTIPLIER',
            field=models.TextField(null=True, verbose_name=b'Array with reccurence                                                         period (interval x                                                         multiplier) for each                                                         product from the order', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_REC_ORIGINAL_REFNO',
            field=models.TextField(null=True, verbose_name=b'Array containing                                                             the reference to                                                             the original order', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_REFERRER',
            field=models.CharField(max_length=250, null=True, verbose_name=b'HTTP referrer of the sale.', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_SHIPPING',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Total amount paid for                                                   shippment', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_TOTAL',
            field=models.TextField(null=True, verbose_name=b'Partial total on order line                                                (including VAT), with                                                period/full-stop (.) as a                                                decimal place separator', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_TOTALGENERAL',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Total transaction                                                       amount, including VAT                                                       costs, with                                                       period/full-stop (.) as                                                       a decimal place                                                       separator', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_VAT',
            field=models.TextField(null=True, verbose_name=b'Array with VAT values per                                product, with period "." as decimal place                                separator', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='IPN_VER',
            field=models.TextField(null=True, verbose_name=b'Array with product versions                                (maximum length: 50 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='LANGUAGE',
            field=models.CharField(max_length=40, null=True, verbose_name=b'The language in which the order                                 has been processed. Possible values: ro,                                 en, fr, de, it.', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='LASTAME_D',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Last Name (maximum length: 40                                  characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='LASTNAME',
            field=models.CharField(max_length=40, null=True, verbose_name=b"Client's last name", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='PAYMETHOD',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Payment method', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='PHONE',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Phone number (maximum length: 40                              characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='PHONE_D',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Phone number (maximum length: 40                                characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='REGISTRATIONNUMBER',
            field=models.CharField(max_length=40, null=True, verbose_name=b"Company's Commerce                                           Registry registration number                                           (maximum length: 40 characters)", blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='STATE',
            field=models.CharField(max_length=30, null=True, verbose_name=b'State/Sector/County (maximum                              length: 30 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='STATE_D',
            field=models.CharField(max_length=30, null=True, verbose_name=b'State/Sector/County (maximum                                length: 30 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='ZIPCODE',
            field=models.CharField(max_length=20, null=True, verbose_name=b'ZIP/Postal Code (maximum length:                                20 characters)', blank=True),
        ),
        migrations.AddField(
            model_name='payuipn',
            name='ZIPCODE_D',
            field=models.CharField(max_length=20, null=True, verbose_name=b'ZIP/Postal Code (maximum                                  length: 20 characters)', blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COMPLETE_DATE',
            field=models.CharField(max_length=40, null=True, verbose_name=b'The order completion date,                                      in the following format: Y-m-d H:i:s                                      (2012-04-26 15:02:28) .', blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='PAYMETHOD_CODE',
            field=models.CharField(max_length=10, verbose_name=b'Payment method code'),
        ),
    ]
