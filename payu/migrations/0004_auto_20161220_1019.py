# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0003_auto_20161220_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payuipn',
            name='ADDRESS1',
            field=models.CharField(help_text=b'Address (maximum length: 100                                 characters)', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ADDRESS1_D',
            field=models.CharField(help_text=b'Address (maximum length: 100                                   characters)', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ADDRESS2',
            field=models.CharField(help_text=b'Additional Address info                                 (maximum length: 100 characters)', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ADDRESS2_D',
            field=models.CharField(help_text=b'Additional address info                                   (maximum length: 100 characters)', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CARD_TYPE',
            field=models.CharField(help_text=b'Used credit card type.                                  Ex: "Visa" or "MasterCard"', max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CBANKACCOUNT',
            field=models.CharField(help_text=b"Company's Bank Account                                     (maximum length: 50 characters)", max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CBANKNAME',
            field=models.CharField(help_text=b"Company's Bank (maximum                                  length: 40 characters) ", max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CITY',
            field=models.CharField(help_text=b'City (maximum length: 30 characters)', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CITY_D',
            field=models.CharField(help_text=b'City (maximum length: 30                               characters)', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COMPANY',
            field=models.CharField(help_text=b'Company name (maximum length:                                              40 characters) ', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COMPANY_D',
            field=models.CharField(help_text=b'Company (maximum length: 50                                  characters)', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COMPLETE_DATE',
            field=models.CharField(help_text=b'The order completion date,                                      in the following format: Y-m-d H:i:s                                      (2012-04-26 15:02:28) .', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COUNTRY',
            field=models.CharField(help_text=b'Country (maximum length: 50                                characters)', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COUNTRY_CODE',
            field=models.CharField(help_text=b'Country (maximum length: 10                                     characters)', max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COUNTRY_D',
            field=models.CharField(help_text=b'Country (maximum length: 50                                  characters)', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COUNTRY_D_CODE',
            field=models.CharField(help_text=b'Country (maximum length:                                       10 characters)', max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CURRENCY',
            field=models.CharField(help_text=b'The currency in which the order                                 has been processed. Possible values: RON,                                 USD, EUR.', max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CUSTOMEREMAIL',
            field=models.CharField(help_text=b"Customer's e-mail address                                      (maximum length: 40 characters)", max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='EMAIL_D',
            field=models.CharField(help_text=b'E-mail (maximum length: 40                                characters)', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='FAX',
            field=models.CharField(help_text=b'Fax number (maximum length: 40                            characters)', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='FIRSTNAME',
            field=models.CharField(help_text=b"Client's first name", max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='FIRSTNAME_D',
            field=models.CharField(help_text=b'First name (maximum length:                                    40 characters) ', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='FISCALCODE',
            field=models.CharField(help_text=b'Unique Registration Number /                                   VAT ID (maximum length: 40 characters)', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IDENTITY_CNP',
            field=models.CharField(help_text=b"Customer's personal numeric                                     code, available only for Romanian customers.", max_length=13, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IDENTITY_ISSUER',
            field=models.CharField(help_text=b'IDENTITY_NO ID Card                                        issuer authority ', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IDENTITY_NO',
            field=models.CharField(help_text=b'Customer ID Card series and                                    number (Series / Number - available                                    only for Romanian customers)', max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPADDRESS',
            field=models.CharField(help_text=b"Client's IP Address (maximum                                  length: 250 characters)", max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPCOUNTRY',
            field=models.CharField(help_text=b"Client's IP Country (maximum                                  length: 50 characters)", max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_COMMISSION',
            field=models.CharField(help_text=b"Payu's commision in RON,                                                     with period/full-stop (.)                                                     as a decimal place                                                     separator.", max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DATE',
            field=models.DateTimeField(help_text=b"IPN POST's sending date in the                                                following format: YmdHis (ex.:                                                20120426145935)", max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DELIVEREDCODES',
            field=models.TextField(help_text=b'Array with the codes                                                         delivered to the                                                         clients, if the PayU                                                         contract contains this                                                         feature. Each element                                                         in the array is                                                         represented by a                                                         string, having comma                                                         (,) as a separator for                                                         each sent code, in                                                         case the ordered                                                         quantity is greater                                                         than 1.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DISCOUNT',
            field=models.TextField(help_text=b'Array with the amounts with                                     which there has been made a discount                                     in a promotion. Including VAT. ', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DOWNLOAD_LINK',
            field=models.CharField(help_text=b'Download link of the                                                        product delivered to                                                        the client', max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_GLOBALDISCOUNT',
            field=models.CharField(help_text=b'Global discount of the                                                         sale. This field is                                                         option and is avaible                                                         only if the amount is                                                         greater than zero.', max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_INFO',
            field=models.TextField(help_text=b'Array with additional                                 information sent for each ordered product (if                                 they have been sent to PayU)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_ORDER_COSTS',
            field=models.TextField(help_text=b"Array with costs for each                                        product from order (expressed in                                        order's currency)", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PCODE',
            field=models.TextField(help_text=b'Array with the product codes                                  assigned by the vendor in the system (vendor                                  reference)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PID',
            field=models.TextField(help_text=b'Array with the ID Codes of the                                ordered products, in the PayU database (PayU                                reference) ', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PNAME',
            field=models.TextField(help_text=b'Array with product names ', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PRICE',
            field=models.TextField(help_text=b'Array with unit prices per                                  product (without VAT), in RON, with                                  period/full-stop (.) as decimal place                                  separator', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PROMOCODE',
            field=models.TextField(help_text=b'Array with the code of the                                      promotions in which the discounts                                      specified above have been made.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PROMONAME',
            field=models.TextField(help_text=b'Array with the names of the                                      promotions in which the discounts                                      specified above have been made.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_QTY',
            field=models.TextField(help_text=b'Array with the product quantities', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_CURRENT_ITERATION_NO',
            field=models.TextField(help_text=b'Current recurring                                                                   period (avaible                                                                   only for recurrent                                                                   payments)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_EXPIRATION_DATE',
            field=models.TextField(help_text=b'Array with                                                              expiration dates                                                              for each                                                              recurrence', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_INTERVAL',
            field=models.TextField(help_text=b'Array containing                                                       recurring intervals                                                       (day/month/week) for                                                       each order', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_MULTIPLIER',
            field=models.TextField(help_text=b'Array with reccurence                                                         period (interval x                                                         multiplier) for each                                                         product from the order', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_ORIGINAL_REFNO',
            field=models.TextField(help_text=b'Array containing                                                             the reference to                                                             the original order', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REFERRER',
            field=models.CharField(help_text=b'HTTP referrer of the sale.', max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_SHIPPING',
            field=models.CharField(help_text=b'Total amount paid for                                                   shippment', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_TOTAL',
            field=models.TextField(help_text=b'Partial total on order line                                                (including VAT), with                                                period/full-stop (.) as a                                                decimal place separator', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_TOTALGENERAL',
            field=models.CharField(help_text=b'Total transaction                                                       amount, including VAT                                                       costs, with                                                       period/full-stop (.) as                                                       a decimal place                                                       separator', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_VAT',
            field=models.TextField(help_text=b'Array with VAT values per                                product, with period "." as decimal place                                separator', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_VER',
            field=models.TextField(help_text=b'Array with product versions                                (maximum length: 50 characters)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='LANGUAGE',
            field=models.CharField(help_text=b'The language in which the order                                 has been processed. Possible values: ro,                                 en, fr, de, it.', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='LASTAME_D',
            field=models.CharField(help_text=b'Last Name (maximum length: 40                                  characters)', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='LASTNAME',
            field=models.CharField(help_text=b"Client's last name", max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='PHONE',
            field=models.CharField(help_text=b'Phone number (maximum length: 40                              characters)', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='PHONE_D',
            field=models.CharField(help_text=b'Phone number (maximum length: 40                                characters)', max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='REGISTRATIONNUMBER',
            field=models.CharField(help_text=b"Company's Commerce                                           Registry registration number                                           (maximum length: 40 characters)", max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='STATE',
            field=models.CharField(help_text=b'State/Sector/County (maximum                              length: 30 characters)', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='STATE_D',
            field=models.CharField(help_text=b'State/Sector/County (maximum                                length: 30 characters)', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ZIPCODE',
            field=models.CharField(help_text=b'ZIP/Postal Code (maximum length:                                20 characters)', max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ZIPCODE_D',
            field=models.CharField(help_text=b'ZIP/Postal Code (maximum                                  length: 20 characters)', max_length=20, null=True, blank=True),
        ),
    ]
