# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0010_auto_20170106_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idn',
            old_name='error',
            new_name='response',
        ),
    ]
