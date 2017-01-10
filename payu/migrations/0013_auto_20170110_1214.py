# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0012_auto_20170109_0820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payuidn',
            options={'verbose_name': 'PayU IDN'},
        ),
        migrations.AlterModelOptions(
            name='payutoken',
            options={'verbose_name': 'PayU Tokens V1'},
        ),
    ]
