# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0009_idn'),
    ]

    operations = [
        migrations.AddField(
            model_name='idn',
            name='error',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='idn',
            name='success',
            field=models.BooleanField(default=False),
        ),
    ]
