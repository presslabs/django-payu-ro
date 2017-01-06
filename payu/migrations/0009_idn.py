# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0008_auto_20170104_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent', models.BooleanField(default=False)),
                ('ipn', models.OneToOneField(to='payu.PayUIPN')),
            ],
        ),
    ]
