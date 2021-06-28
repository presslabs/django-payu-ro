# Generated by Django 3.1.12 on 2021-06-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0003_auto_20200820_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payuipn',
            name='ADDRESS1',
            field=models.CharField(blank=True, help_text='Address (maximum length: 100                                 characters)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ADDRESS1_D',
            field=models.CharField(blank=True, help_text='Address (maximum length: 100                                   characters)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ADDRESS2',
            field=models.CharField(blank=True, help_text='Additional Address info                                 (maximum length: 100 characters)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ADDRESS2_D',
            field=models.CharField(blank=True, help_text='Additional address info                                   (maximum length: 100 characters)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CARD_TYPE',
            field=models.CharField(blank=True, help_text='Used credit card type.                                  Ex: "Visa" or "MasterCard"', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CBANKACCOUNT',
            field=models.CharField(blank=True, help_text="Company's Bank Account                                     (maximum length: 50 characters)", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CBANKNAME',
            field=models.CharField(blank=True, help_text="Company's Bank (maximum                                  length: 40 characters) ", max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CITY',
            field=models.CharField(blank=True, help_text='City (maximum length: 30 characters)', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CITY_D',
            field=models.CharField(blank=True, help_text='City (maximum length: 30                               characters)', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COMPANY',
            field=models.CharField(blank=True, help_text='Company name (maximum length:                                              40 characters) ', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COMPANY_D',
            field=models.CharField(blank=True, help_text='Company (maximum length: 50                                  characters)', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COMPLETE_DATE',
            field=models.CharField(blank=True, help_text='The order completion date,                                      in the following format: Y-m-d H:i:s                                      (2012-04-26 15:02:28) .', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COUNTRY',
            field=models.CharField(blank=True, help_text='Country (maximum length: 50                                characters)', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COUNTRY_CODE',
            field=models.CharField(blank=True, help_text='Country (maximum length: 10                                     characters)', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COUNTRY_D',
            field=models.CharField(blank=True, help_text='Country (maximum length: 50                                  characters)', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='COUNTRY_D_CODE',
            field=models.CharField(blank=True, help_text='Country (maximum length:                                       10 characters)', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CURRENCY',
            field=models.CharField(blank=True, help_text='The currency in which the order                                 has been processed. Possible values: RON,                                 USD, EUR.', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='CUSTOMEREMAIL',
            field=models.CharField(blank=True, help_text="Customer's e-mail address                                      (maximum length: 40 characters)", max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='EMAIL_D',
            field=models.CharField(blank=True, help_text='E-mail (maximum length: 40                                characters)', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='FAX',
            field=models.CharField(blank=True, help_text='Fax number (maximum length: 40                            characters)', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='FIRSTNAME',
            field=models.CharField(blank=True, help_text="Client's first name", max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='FIRSTNAME_D',
            field=models.CharField(blank=True, help_text='First name (maximum length:                                    40 characters) ', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='FISCALCODE',
            field=models.CharField(blank=True, help_text='Unique Registration Number /                                   VAT ID (maximum length: 40 characters)', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IDENTITY_CNP',
            field=models.CharField(blank=True, help_text="Customer's personal numeric                                     code, available only for Romanian customers.", max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IDENTITY_ISSUER',
            field=models.CharField(blank=True, help_text='IDENTITY_NO ID Card                                        issuer authority ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IDENTITY_NO',
            field=models.CharField(blank=True, help_text='Customer ID Card series and                                    number (Series / Number - available                                    only for Romanian customers)', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPADDRESS',
            field=models.CharField(blank=True, help_text="Client's IP Address (maximum                                  length: 250 characters)", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPCOUNTRY',
            field=models.CharField(blank=True, help_text="Client's IP Country (maximum                                  length: 50 characters)", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_COMMISSION',
            field=models.CharField(blank=True, help_text="Payu's commision in RON,                                                     with period/full-stop (.)                                                     as a decimal place                                                     separator.", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DATE',
            field=models.DateTimeField(blank=True, help_text="IPN POST's sending date in the                                                following format: YmdHMS (ex.:                                                20120426145935)", max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DELIVEREDCODES',
            field=models.TextField(blank=True, help_text='Array with the codes                                                         delivered to the                                                         clients, if the PayU                                                         contract contains this                                                         feature. Each element                                                         in the array is                                                         represented by a                                                         string, having comma                                                         (,) as a separator for                                                         each sent code, in                                                         case the ordered                                                         quantity is greater                                                         than 1.', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DISCOUNT',
            field=models.TextField(blank=True, help_text='Array with the amounts with                                     which there has been made a discount                                     in a promotion. Including VAT. ', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_DOWNLOAD_LINK',
            field=models.CharField(blank=True, help_text='Download link of the                                                        product delivered to                                                        the client', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_GLOBALDISCOUNT',
            field=models.CharField(blank=True, help_text='Global discount of the                                                         sale. This field is                                                         option and is avaible                                                         only if the amount is                                                         greater than zero.', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_INFO',
            field=models.TextField(blank=True, help_text='Array with additional                                 information sent for each ordered product (if                                 they have been sent to PayU)', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_ORDER_COSTS',
            field=models.TextField(blank=True, help_text="Array with costs for each                                        product from order (expressed in                                        order's currency)", null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PCODE',
            field=models.TextField(blank=True, help_text='Array with the product codes                                  assigned by the vendor in the system (vendor                                  reference)', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PID',
            field=models.TextField(blank=True, help_text='Array with the ID Codes of the                                ordered products, in the PayU database (PayU                                reference) ', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PNAME',
            field=models.TextField(blank=True, help_text='Array with product names ', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PRICE',
            field=models.TextField(blank=True, help_text='Array with unit prices per                                  product (without VAT), in RON, with                                  period/full-stop (.) as decimal place                                  separator', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PROMOCODE',
            field=models.TextField(blank=True, help_text='Array with the code of the                                      promotions in which the discounts                                      specified above have been made.', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_PROMONAME',
            field=models.TextField(blank=True, help_text='Array with the names of the                                      promotions in which the discounts                                      specified above have been made.', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_QTY',
            field=models.TextField(blank=True, help_text='Array with the product quantities', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_CURRENT_ITERATION_NO',
            field=models.TextField(blank=True, help_text='Current recurring                                                                   period (avaible                                                                   only for recurrent                                                                   payments)', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_EXPIRATION_DATE',
            field=models.TextField(blank=True, help_text='Array with                                                              expiration dates                                                              for each                                                              recurrence', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_INTERVAL',
            field=models.TextField(blank=True, help_text='Array containing                                                       recurring intervals                                                       (day/month/week) for                                                       each order', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_MULTIPLIER',
            field=models.TextField(blank=True, help_text='Array with reccurence                                                         period (interval x                                                         multiplier) for each                                                         product from the order', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REC_ORIGINAL_REFNO',
            field=models.TextField(blank=True, help_text='Array containing                                                             the reference to                                                             the original order', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_REFERRER',
            field=models.CharField(blank=True, help_text='HTTP referrer of the sale.', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_SHIPPING',
            field=models.CharField(blank=True, help_text='Total amount paid for                                                   shippment', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_TOTAL',
            field=models.TextField(blank=True, help_text='Partial total on order line                                                (including VAT), with                                                period/full-stop (.) as a                                                decimal place separator', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_TOTALGENERAL',
            field=models.CharField(blank=True, help_text='Total transaction                                                       amount, including VAT                                                       costs, with                                                       period/full-stop (.) as                                                       a decimal place                                                       separator', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_VAT',
            field=models.TextField(blank=True, help_text='Array with VAT values per                                product, with period "." as decimal place                                separator', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='IPN_VER',
            field=models.TextField(blank=True, help_text='Array with product versions                                (maximum length: 50 characters)', null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='LANGUAGE',
            field=models.CharField(blank=True, help_text='The language in which the order                                 has been processed. Possible values: ro,                                 en, fr, de, it.', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='LASTAME_D',
            field=models.CharField(blank=True, help_text='Last Name (maximum length: 40                                  characters)', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='LASTNAME',
            field=models.CharField(blank=True, help_text="Client's last name", max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ORDERNO',
            field=models.CharField(max_length=6, verbose_name='Merchant order #'),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ORDERSTATUS',
            field=models.CharField(choices=[('PAYMENT_AUTHORIZED', 'PAYMENT_AUTHORIZED'), ('PAYMENT_RECEIVED', 'PAYMENT_RECEIVED'), ('TEST', 'TEST'), ('CASH', 'CASH'), ('COMPLETE', 'COMPLETE'), ('REVERSED', 'REVERSED'), ('REFUND', 'REFUND')], max_length=18, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='PAYMENTDATE',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Payment date'),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='PAYMETHOD',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Payment method'),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='PAYMETHOD_CODE',
            field=models.CharField(max_length=10, verbose_name='Payment method code'),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='PHONE',
            field=models.CharField(blank=True, help_text='Phone number (maximum length: 40                              characters)', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='PHONE_D',
            field=models.CharField(blank=True, help_text='Phone number (maximum length: 40                                characters)', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='REFNO',
            field=models.CharField(max_length=9, verbose_name='ePayment reference'),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='REFNOEXT',
            field=models.CharField(max_length=100, verbose_name='Merchant reference'),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='REGISTRATIONNUMBER',
            field=models.CharField(blank=True, help_text="Company's Commerce                                           Registry registration number                                           (maximum length: 40 characters)", max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='SALEDATE',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Sale date'),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='STATE',
            field=models.CharField(blank=True, help_text='State/Sector/County (maximum                              length: 30 characters)', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='STATE_D',
            field=models.CharField(blank=True, help_text='State/Sector/County (maximum                                length: 30 characters)', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ZIPCODE',
            field=models.CharField(blank=True, help_text='ZIP/Postal Code (maximum length:                                20 characters)', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payuipn',
            name='ZIPCODE_D',
            field=models.CharField(blank=True, help_text='ZIP/Postal Code (maximum                                  length: 20 characters)', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payutoken',
            name='IPN_CC_EXP_DATE',
            field=models.DateField(verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='payutoken',
            name='IPN_CC_MASK',
            field=models.CharField(max_length=36, verbose_name='Last 4 digits'),
        ),
        migrations.AlterField(
            model_name='payutoken',
            name='IPN_CC_TOKEN',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Token (deprecated)'),
        ),
        migrations.AlterField(
            model_name='payutoken',
            name='TOKEN_HASH',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Token'),
        ),
    ]
