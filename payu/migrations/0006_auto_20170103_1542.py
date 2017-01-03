# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0005_auto_20161229_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payuipn',
            name='CARD_TYPE',
            field=models.CharField(help_text=b'Used credit card type.                                  Ex: "Visa" or "MasterCard"', max_length=100, null=True, blank=True),
        ),
    ]
