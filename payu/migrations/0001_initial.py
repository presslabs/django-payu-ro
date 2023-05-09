# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PayUIDN",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("sent", models.BooleanField(default=False)),
                ("success", models.BooleanField(default=False)),
                ("response", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "PayU IDN",
            },
        ),
        migrations.CreateModel(
            name="PayUIPN",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "REFNO",
                    models.CharField(max_length=9, verbose_name=b"ePayment reference"),
                ),
                (
                    "REFNOEXT",
                    models.CharField(
                        max_length=100, verbose_name=b"Merchant reference"
                    ),
                ),
                (
                    "ORDERNO",
                    models.CharField(max_length=6, verbose_name=b"Merchant order #"),
                ),
                (
                    "ORDERSTATUS",
                    models.CharField(
                        max_length=18,
                        verbose_name=b"Status",
                        choices=[
                            (b"PAYMENT_AUTHORIZED", b"PAYMENT_AUTHORIZED"),
                            (b"PAYMENT_RECEIVED", b"PAYMENT_RECEIVED"),
                            (b"TEST", b"TEST"),
                            (b"CASH", b"CASH"),
                            (b"COMPLETE", b"COMPLETE"),
                            (b"REVERSED", b"REVERSED"),
                            (b"REFUND", b"REFUND"),
                        ],
                    ),
                ),
                ("HASH", models.CharField(max_length=64)),
                (
                    "PAYMETHOD_CODE",
                    models.CharField(
                        max_length=10, verbose_name=b"Payment method code"
                    ),
                ),
                (
                    "SALEDATE",
                    models.DateTimeField(
                        null=True, verbose_name=b"Sale date", blank=True
                    ),
                ),
                (
                    "PAYMENTDATE",
                    models.DateTimeField(
                        null=True, verbose_name=b"Payment date", blank=True
                    ),
                ),
                (
                    "PAYMETHOD",
                    models.CharField(
                        max_length=100,
                        null=True,
                        verbose_name=b"Payment method",
                        blank=True,
                    ),
                ),
                (
                    "FIRSTNAME",
                    models.CharField(
                        help_text=b"Client's first name",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "LASTNAME",
                    models.CharField(
                        help_text=b"Client's last name",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IDENTITY_NO",
                    models.CharField(
                        help_text=b"Customer ID Card series and                                    number (Series / Number - available                                    only for Romanian customers)",
                        max_length=15,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IDENTITY_ISSUER",
                    models.CharField(
                        help_text=b"IDENTITY_NO ID Card                                        issuer authority ",
                        max_length=100,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "CARD_TYPE",
                    models.CharField(
                        help_text=b'Used credit card type.                                  Ex: "Visa" or "MasterCard"',
                        max_length=100,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IDENTITY_CNP",
                    models.CharField(
                        help_text=b"Customer's personal numeric                                     code, available only for Romanian customers.",
                        max_length=13,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "COMPANY",
                    models.CharField(
                        help_text=b"Company name (maximum length:                                              40 characters) ",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "REGISTRATIONNUMBER",
                    models.CharField(
                        help_text=b"Company's Commerce                                           Registry registration number                                           (maximum length: 40 characters)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "FISCALCODE",
                    models.CharField(
                        help_text=b"Unique Registration Number /                                   VAT ID (maximum length: 40 characters)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "CBANKNAME",
                    models.CharField(
                        help_text=b"Company's Bank (maximum                                  length: 40 characters) ",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "CBANKACCOUNT",
                    models.CharField(
                        help_text=b"Company's Bank Account                                     (maximum length: 50 characters)",
                        max_length=50,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "ADDRESS1",
                    models.CharField(
                        help_text=b"Address (maximum length: 100                                 characters)",
                        max_length=100,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "ADDRESS2",
                    models.CharField(
                        help_text=b"Additional Address info                                 (maximum length: 100 characters)",
                        max_length=100,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "CITY",
                    models.CharField(
                        help_text=b"City (maximum length: 30 characters)",
                        max_length=30,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "STATE",
                    models.CharField(
                        help_text=b"State/Sector/County (maximum                              length: 30 characters)",
                        max_length=30,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "ZIPCODE",
                    models.CharField(
                        help_text=b"ZIP/Postal Code (maximum length:                                20 characters)",
                        max_length=20,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "COUNTRY",
                    models.CharField(
                        help_text=b"Country (maximum length: 50                                characters)",
                        max_length=50,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "COUNTRY_CODE",
                    models.CharField(
                        help_text=b"Country (maximum length: 10                                     characters)",
                        max_length=10,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "PHONE",
                    models.CharField(
                        help_text=b"Phone number (maximum length: 40                              characters)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "FAX",
                    models.CharField(
                        help_text=b"Fax number (maximum length: 40                            characters)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "CUSTOMEREMAIL",
                    models.CharField(
                        help_text=b"Customer's e-mail address                                      (maximum length: 40 characters)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "FIRSTNAME_D",
                    models.CharField(
                        help_text=b"First name (maximum length:                                    40 characters) ",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "LASTAME_D",
                    models.CharField(
                        help_text=b"Last Name (maximum length: 40                                  characters)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "COMPANY_D",
                    models.CharField(
                        help_text=b"Company (maximum length: 50                                  characters)",
                        max_length=50,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "ADDRESS1_D",
                    models.CharField(
                        help_text=b"Address (maximum length: 100                                   characters)",
                        max_length=100,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "ADDRESS2_D",
                    models.CharField(
                        help_text=b"Additional address info                                   (maximum length: 100 characters)",
                        max_length=100,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "CITY_D",
                    models.CharField(
                        help_text=b"City (maximum length: 30                               characters)",
                        max_length=30,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "STATE_D",
                    models.CharField(
                        help_text=b"State/Sector/County (maximum                                length: 30 characters)",
                        max_length=30,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "ZIPCODE_D",
                    models.CharField(
                        help_text=b"ZIP/Postal Code (maximum                                  length: 20 characters)",
                        max_length=20,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "COUNTRY_D",
                    models.CharField(
                        help_text=b"Country (maximum length: 50                                  characters)",
                        max_length=50,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "COUNTRY_D_CODE",
                    models.CharField(
                        help_text=b"Country (maximum length:                                       10 characters)",
                        max_length=10,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "PHONE_D",
                    models.CharField(
                        help_text=b"Phone number (maximum length: 40                                characters)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "EMAIL_D",
                    models.CharField(
                        help_text=b"E-mail (maximum length: 40                                characters)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPADDRESS",
                    models.CharField(
                        help_text=b"Client's IP Address (maximum                                  length: 250 characters)",
                        max_length=250,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPCOUNTRY",
                    models.CharField(
                        help_text=b"Client's IP Country (maximum                                  length: 50 characters)",
                        max_length=50,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "COMPLETE_DATE",
                    models.CharField(
                        help_text=b"The order completion date,                                      in the following format: Y-m-d H:i:s                                      (2012-04-26 15:02:28) .",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "CURRENCY",
                    models.CharField(
                        help_text=b"The currency in which the order                                 has been processed. Possible values: RON,                                 USD, EUR.",
                        max_length=10,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "LANGUAGE",
                    models.CharField(
                        help_text=b"The language in which the order                                 has been processed. Possible values: ro,                                 en, fr, de, it.",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_PID",
                    models.TextField(
                        help_text=b"Array with the ID Codes of the                                ordered products, in the PayU database (PayU                                reference) ",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_PNAME",
                    models.TextField(
                        help_text=b"Array with product names ", null=True, blank=True
                    ),
                ),
                (
                    "IPN_PCODE",
                    models.TextField(
                        help_text=b"Array with the product codes                                  assigned by the vendor in the system (vendor                                  reference)",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_INFO",
                    models.TextField(
                        help_text=b"Array with additional                                 information sent for each ordered product (if                                 they have been sent to PayU)",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_QTY",
                    models.TextField(
                        help_text=b"Array with the product quantities",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_PRICE",
                    models.TextField(
                        help_text=b"Array with unit prices per                                  product (without VAT), in RON, with                                  period/full-stop (.) as decimal place                                  separator",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_VAT",
                    models.TextField(
                        help_text=b'Array with VAT values per                                product, with period "." as decimal place                                separator',
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_VER",
                    models.TextField(
                        help_text=b"Array with product versions                                (maximum length: 50 characters)",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_DISCOUNT",
                    models.TextField(
                        help_text=b"Array with the amounts with                                     which there has been made a discount                                     in a promotion. Including VAT. ",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_PROMONAME",
                    models.TextField(
                        help_text=b"Array with the names of the                                      promotions in which the discounts                                      specified above have been made.",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_PROMOCODE",
                    models.TextField(
                        help_text=b"Array with the code of the                                      promotions in which the discounts                                      specified above have been made.",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_ORDER_COSTS",
                    models.TextField(
                        help_text=b"Array with costs for each                                        product from order (expressed in                                        order's currency)",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_REC_CURRENT_ITERATION_NO",
                    models.TextField(
                        help_text=b"Current recurring                                                                   period (avaible                                                                   only for recurrent                                                                   payments)",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_REC_ORIGINAL_REFNO",
                    models.TextField(
                        help_text=b"Array containing                                                             the reference to                                                             the original order",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_REC_INTERVAL",
                    models.TextField(
                        help_text=b"Array containing                                                       recurring intervals                                                       (day/month/week) for                                                       each order",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_REC_EXPIRATION_DATE",
                    models.TextField(
                        help_text=b"Array with                                                              expiration dates                                                              for each                                                              recurrence",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_REC_MULTIPLIER",
                    models.TextField(
                        help_text=b"Array with reccurence                                                         period (interval x                                                         multiplier) for each                                                         product from the order",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_DELIVEREDCODES",
                    models.TextField(
                        help_text=b"Array with the codes                                                         delivered to the                                                         clients, if the PayU                                                         contract contains this                                                         feature. Each element                                                         in the array is                                                         represented by a                                                         string, having comma                                                         (,) as a separator for                                                         each sent code, in                                                         case the ordered                                                         quantity is greater                                                         than 1.",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_DOWNLOAD_LINK",
                    models.CharField(
                        help_text=b"Download link of the                                                        product delivered to                                                        the client",
                        max_length=250,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_TOTAL",
                    models.TextField(
                        help_text=b"Partial total on order line                                                (including VAT), with                                                period/full-stop (.) as a                                                decimal place separator",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_TOTALGENERAL",
                    models.CharField(
                        help_text=b"Total transaction                                                       amount, including VAT                                                       costs, with                                                       period/full-stop (.) as                                                       a decimal place                                                       separator",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_SHIPPING",
                    models.CharField(
                        help_text=b"Total amount paid for                                                   shippment",
                        max_length=50,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_REFERRER",
                    models.CharField(
                        help_text=b"HTTP referrer of the sale.",
                        max_length=250,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_GLOBALDISCOUNT",
                    models.CharField(
                        help_text=b"Global discount of the                                                         sale. This field is                                                         option and is avaible                                                         only if the amount is                                                         greater than zero.",
                        max_length=250,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_COMMISSION",
                    models.CharField(
                        help_text=b"Payu's commision in RON,                                                     with period/full-stop (.)                                                     as a decimal place                                                     separator.",
                        max_length=50,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "IPN_DATE",
                    models.DateTimeField(
                        help_text=b"IPN POST's sending date in the                                                following format: YmdHMS (ex.:                                                20120426145935)",
                        max_length=40,
                        null=True,
                        blank=True,
                    ),
                ),
                ("response", models.TextField(blank=True)),
                ("ip_address", models.GenericIPAddressField(null=True, blank=True)),
                ("flag", models.BooleanField(default=False)),
                ("flag_info", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "payu_ipn",
                "verbose_name": "PayU IPN",
            },
        ),
        migrations.CreateModel(
            name="PayUToken",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("IPN_CC_TOKEN", models.CharField(max_length=9, verbose_name=b"Token")),
                (
                    "IPN_CC_MASK",
                    models.CharField(max_length=36, verbose_name=b"Last 4 digits"),
                ),
                ("IPN_CC_EXP_DATE", models.DateField(verbose_name=b"Expiration date")),
                (
                    "ipn",
                    models.OneToOneField(to="payu.PayUIPN", on_delete=models.CASCADE),
                ),
            ],
            options={
                "verbose_name": "PayU Tokens V1",
            },
        ),
        migrations.AddField(
            model_name="payuidn",
            name="ipn",
            field=models.OneToOneField(to="payu.PayUIPN", on_delete=models.CASCADE),
        ),
    ]
