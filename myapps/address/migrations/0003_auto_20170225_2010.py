# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20170225_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='detail_address',
        ),
    ]
